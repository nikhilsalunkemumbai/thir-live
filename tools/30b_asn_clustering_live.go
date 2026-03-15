// Tool 30 Extension — ASN Clustering
// THIR · nikhilsalunkemumbai/thir-live
// Input:  data/threat_ips.json
// Output: data/asn_clusters.json
//
// Groups attacker IPs from threat_ips.json by ASN.
// Pure aggregation on existing data — no new API calls.
// Run as standalone: go run tools/30b_asn_clustering_live.go
// Or integrated: called directly from pipeline after Tool 30.

package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
	"time"
)

// ── Input schema (threat_ips.json) ──────────────────────────────────────────

type ThreatIP struct {
	IP          string  `json:"indicator"`
	AbuseScore  int     `json:"abuse_score"`
	TotalReports int    `json:"total_reports"`
	Country     string  `json:"country"`
	CountryCode string  `json:"country_code"`
	ISP         string  `json:"isp"`
	Domain      string  `json:"domain"`
	Org         string  `json:"org"`
	ASN         string  `json:"asn"`
	ASNName     string  `json:"asn_name"`
	IsTor       bool    `json:"is_tor"`
	IsProxy     bool    `json:"is_proxy"`
	IsVPN       bool    `json:"is_vpn"`
	RiskLevel   string  `json:"risk_level"`
	Tags        []string `json:"tags"`
	LastSeen    string  `json:"last_seen"`
}

type ThreatIPFile struct {
	GeneratedAt string     `json:"generated_at"`
	TotalIPs    int        `json:"total_ips"`
	IPs         []ThreatIP `json:"ips"`
}

// ── Output schema ────────────────────────────────────────────────────────────

type ASNCluster struct {
	ASN              string   `json:"asn"`
	ASNName          string   `json:"asn_name"`
	IPCount          int      `json:"ip_count"`
	UniqueIPs        []string `json:"unique_ips"`
	Countries        []string `json:"countries"`
	TopCountry       string   `json:"top_country"`
	AvgAbuseScore    float64  `json:"avg_abuse_score"`
	MaxAbuseScore    int      `json:"max_abuse_score"`
	TotalReports     int      `json:"total_reports"`
	TorCount         int      `json:"tor_count"`
	ProxyCount       int      `json:"proxy_count"`
	VPNCount         int      `json:"vpn_count"`
	AnonCount        int      `json:"anon_count"` // tor+proxy+vpn
	HighRiskCount    int      `json:"high_risk_count"`
	CriticalCount    int      `json:"critical_count"`
	RiskTier         string   `json:"risk_tier"` // HIGH / MEDIUM / LOW
	Tags             []string `json:"tags"`
	FirstSeen        string   `json:"first_seen"`
	LastSeen         string   `json:"last_seen"`
	ISPs             []string `json:"isps"`
}

type ProviderSummary struct {
	ASN        string `json:"asn"`
	ASNName    string `json:"asn_name"`
	IPCount    int    `json:"ip_count"`
	RiskTier   string `json:"risk_tier"`
	AnonCount  int    `json:"anon_count"`
}

type ASNClusters struct {
	GeneratedAt      string            `json:"generated_at"`
	SourceFile       string            `json:"source_file"`
	TotalIPsAnalyzed int               `json:"total_ips_analyzed"`
	UniqueASNs       int               `json:"unique_asns"`
	TopAttackASNs    []ProviderSummary `json:"top_attack_asns"`
	HighRiskASNs     []ProviderSummary `json:"high_risk_asns"`
	AnonInfra        []ProviderSummary `json:"anon_infrastructure"` // heavy tor/vpn/proxy
	CountrySummary   []CountryCount    `json:"country_summary"`
	Clusters         []ASNCluster      `json:"clusters"`
}

type CountryCount struct {
	Country string `json:"country"`
	Code    string `json:"code"`
	Count   int    `json:"count"`
}

// ── Helpers ──────────────────────────────────────────────────────────────────

func uniqueStrings(slice []string) []string {
	seen := make(map[string]struct{})
	out := []string{}
	for _, s := range slice {
		if s == "" {
			continue
		}
		if _, ok := seen[s]; !ok {
			seen[s] = struct{}{}
			out = append(out, s)
		}
	}
	sort.Strings(out)
	return out
}

func topString(counts map[string]int) string {
	best, bestCount := "", 0
	for k, v := range counts {
		if v > bestCount || (v == bestCount && k < best) {
			best, bestCount = k, v
		}
	}
	return best
}

func riskTier(cluster *ASNCluster) string {
	if cluster.CriticalCount > 0 || cluster.MaxAbuseScore >= 90 || cluster.AnonCount > cluster.IPCount/2 {
		return "HIGH"
	}
	if cluster.HighRiskCount > 0 || cluster.AvgAbuseScore >= 50 || cluster.AnonCount > 0 {
		return "MEDIUM"
	}
	return "LOW"
}

func clusterTags(cluster *ASNCluster) []string {
	tags := []string{}
	if cluster.TorCount > 0 {
		tags = append(tags, "tor-exit")
	}
	if cluster.ProxyCount > 0 {
		tags = append(tags, "proxy")
	}
	if cluster.VPNCount > 0 {
		tags = append(tags, "vpn")
	}
	if cluster.AnonCount >= 3 {
		tags = append(tags, "anon-infrastructure")
	}
	if cluster.MaxAbuseScore >= 90 {
		tags = append(tags, "high-abuse")
	}
	if cluster.CriticalCount > 0 {
		tags = append(tags, "critical-ips")
	}
	if cluster.IPCount >= 10 {
		tags = append(tags, "bulk-attacker")
	}
	if strings.Contains(strings.ToLower(cluster.ASNName), "cloud") ||
		strings.Contains(strings.ToLower(cluster.ASNName), "amazon") ||
		strings.Contains(strings.ToLower(cluster.ASNName), "azure") ||
		strings.Contains(strings.ToLower(cluster.ASNName), "google") ||
		strings.Contains(strings.ToLower(cluster.ASNName), "digital ocean") ||
		strings.Contains(strings.ToLower(cluster.ASNName), "linode") ||
		strings.Contains(strings.ToLower(cluster.ASNName), "vultr") ||
		strings.Contains(strings.ToLower(cluster.ASNName), "hetzner") ||
		strings.Contains(strings.ToLower(cluster.ASNName), "ovh") {
		tags = append(tags, "cloud-provider")
	}
	if strings.Contains(strings.ToLower(cluster.ASNName), "hosting") {
		tags = append(tags, "hosting-provider")
	}
	return tags
}

func providerSummary(cluster ASNCluster) ProviderSummary {
	return ProviderSummary{
		ASN:       cluster.ASN,
		ASNName:   cluster.ASNName,
		IPCount:   cluster.IPCount,
		RiskTier:  cluster.RiskTier,
		AnonCount: cluster.AnonCount,
	}
}

// ── Main logic ───────────────────────────────────────────────────────────────

func main() {
	input := flag.String("input", "data/threat_ips.json", "Path to threat_ips.json")
	output := flag.String("output", "data/asn_clusters.json", "Output path")
	flag.Parse()

	log.Printf("[Tool30b] Reading %s", *input)

	data, err := os.ReadFile(*input)
	if err != nil {
		log.Fatalf("[Tool30b] Cannot read %s: %v", *input, err)
	}

	var tipFile ThreatIPFile
	if err := json.Unmarshal(data, &tipFile); err != nil {
		// Try as plain array
		var ips []ThreatIP
		if err2 := json.Unmarshal(data, &ips); err2 != nil {
			log.Fatalf("[Tool30b] Cannot parse %s: %v", *input, err)
		}
		tipFile.IPs = ips
	}

	log.Printf("[Tool30b] Loaded %d IPs", len(tipFile.IPs))

	// ── Build ASN map ────────────────────────────────────────────────────────
	type asnAccum struct {
		asnName     string
		ips         []string
		countries   []string
		countryCounts map[string]int
		abuseScores []int
		totalReports int
		torCount    int
		proxyCount  int
		vpnCount    int
		highRisk    int
		critical    int
		timestamps  []string
		isps        []string
	}

	asnMap := make(map[string]*asnAccum)
	countryMap := make(map[string]struct{ code string; count int })

	for _, ip := range tipFile.IPs {
		asn := ip.ASN
		if asn == "" {
			asn = "AS0"
		}

		if _, ok := asnMap[asn]; !ok {
			asnMap[asn] = &asnAccum{
				asnName:       ip.ASNName,
				countryCounts: make(map[string]int),
			}
		}
		acc := asnMap[asn]

		if acc.asnName == "" {
			acc.asnName = ip.ASNName
		}
		acc.ips = append(acc.ips, ip.IP)
		if ip.Country != "" {
			acc.countries = append(acc.countries, ip.Country)
			acc.countryCounts[ip.Country]++
		}
		acc.abuseScores = append(acc.abuseScores, ip.AbuseScore)
		acc.totalReports += ip.TotalReports
		if ip.IsTor {
			acc.torCount++
		}
		if ip.IsProxy {
			acc.proxyCount++
		}
		if ip.IsVPN {
			acc.vpnCount++
		}
		risk := strings.ToUpper(ip.RiskLevel)
		if risk == "HIGH" {
			acc.highRisk++
		}
		if risk == "CRITICAL" {
			acc.critical++
		}
		if ip.LastSeen != "" {
			acc.timestamps = append(acc.timestamps, ip.LastSeen)
		}
		if ip.ISP != "" {
			acc.isps = append(acc.isps, ip.ISP)
		}

		// Country summary
		cc := countryMap[ip.Country]
		cc.code = ip.CountryCode
		cc.count++
		countryMap[ip.Country] = cc
	}

	// ── Convert to clusters ──────────────────────────────────────────────────
	clusters := []ASNCluster{}
	for asn, acc := range asnMap {
		// Avg abuse score
		avgAbuse := 0.0
		maxAbuse := 0
		for _, s := range acc.abuseScores {
			avgAbuse += float64(s)
			if s > maxAbuse {
				maxAbuse = s
			}
		}
		if len(acc.abuseScores) > 0 {
			avgAbuse /= float64(len(acc.abuseScores))
		}

		// Timestamps
		firstSeen, lastSeen := "", ""
		if len(acc.timestamps) > 0 {
			sort.Strings(acc.timestamps)
			firstSeen = acc.timestamps[0]
			lastSeen = acc.timestamps[len(acc.timestamps)-1]
		}

		cl := ASNCluster{
			ASN:           asn,
			ASNName:       acc.asnName,
			IPCount:       len(uniqueStrings(acc.ips)),
			UniqueIPs:     uniqueStrings(acc.ips),
			Countries:     uniqueStrings(acc.countries),
			TopCountry:    topString(acc.countryCounts),
			AvgAbuseScore: avgAbuse,
			MaxAbuseScore: maxAbuse,
			TotalReports:  acc.totalReports,
			TorCount:      acc.torCount,
			ProxyCount:    acc.proxyCount,
			VPNCount:      acc.vpnCount,
			AnonCount:     acc.torCount + acc.proxyCount + acc.vpnCount,
			HighRiskCount: acc.highRisk,
			CriticalCount: acc.critical,
			FirstSeen:     firstSeen,
			LastSeen:      lastSeen,
			ISPs:          uniqueStrings(acc.isps),
		}
		cl.RiskTier = riskTier(&cl)
		cl.Tags = clusterTags(&cl)
		clusters = append(clusters, cl)
	}

	// Sort clusters by IP count descending
	sort.Slice(clusters, func(i, j int) bool {
		return clusters[i].IPCount > clusters[j].IPCount
	})

	// ── Top lists ─────────────────────────────────────────────────────────────
	topN := 10
	topASNs := []ProviderSummary{}
	highRiskASNs := []ProviderSummary{}
	anonInfra := []ProviderSummary{}

	for _, cl := range clusters {
		if len(topASNs) < topN {
			topASNs = append(topASNs, providerSummary(cl))
		}
		if cl.RiskTier == "HIGH" {
			highRiskASNs = append(highRiskASNs, providerSummary(cl))
		}
		if cl.AnonCount >= 2 {
			anonInfra = append(anonInfra, providerSummary(cl))
		}
	}

	// Country summary
	type cc struct {
		country string
		code    string
		count   int
	}
	ccList := []cc{}
	for country, data := range countryMap {
		ccList = append(ccList, cc{country, data.code, data.count})
	}
	sort.Slice(ccList, func(i, j int) bool { return ccList[i].count > ccList[j].count })
	countrySummary := []CountryCount{}
	for _, c := range ccList {
		countrySummary = append(countrySummary, CountryCount{c.country, c.code, c.count})
	}

	// ── Output ────────────────────────────────────────────────────────────────
	result := ASNClusters{
		GeneratedAt:      time.Now().UTC().Format(time.RFC3339),
		SourceFile:       *input,
		TotalIPsAnalyzed: len(tipFile.IPs),
		UniqueASNs:       len(clusters),
		TopAttackASNs:    topASNs,
		HighRiskASNs:     highRiskASNs,
		AnonInfra:        anonInfra,
		CountrySummary:   countrySummary,
		Clusters:         clusters,
	}

	// Ensure output directory exists
	outputPath := *output
	dir := outputPath[:strings.LastIndex(outputPath, "/")+1]
	if dir != "" {
		if err := os.MkdirAll(dir, 0755); err != nil {
			log.Fatalf("[Tool30b] Cannot create output dir: %v", err)
		}
	}

	outData, err := json.MarshalIndent(result, "", "  ")
	if err != nil {
		log.Fatalf("[Tool30b] JSON marshal error: %v", err)
	}
	if err := os.WriteFile(outputPath, outData, 0644); err != nil {
		log.Fatalf("[Tool30b] Cannot write output: %v", err)
	}

	fmt.Printf("[Tool30b] ✓ Written → %s\n", outputPath)
	fmt.Printf("[Tool30b]   IPs: %d | ASNs: %d | High-risk ASNs: %d | Anon infra: %d\n",
		len(tipFile.IPs), len(clusters), len(highRiskASNs), len(anonInfra))
	if len(clusters) > 0 {
		top := clusters[0]
		fmt.Printf("[Tool30b]   Top ASN: %s (%s) — %d IPs [%s]\n",
			top.ASN, top.ASNName, top.IPCount, top.RiskTier)
	}
}
