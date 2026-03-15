// 30_metric_exporter_live.go
//
// THIR LIVE PIPELINE — PRODUCTION TOOL
// Adapted from: InfraReadyPortfolio/06_soc_collaboration_tools/30_security_metric_dashboard_exporter/
//
// CHANGES FROM ORIGINAL (security_metric_dashboard_exporter.go):
//   1. Metric struct EXTENDED — added ValueInt, ValueFloat, Category fields
//      Original Source/Name/Value string fields preserved as-is
//
//   2. DashboardStats struct NEW — aggregated view of entire pipeline run
//      Pulls from all four pipeline data files (Tools 26, 27, 29, 05)
//
//   3. discoverFiles()    KEPT AS-IS — filepath.Glob wrapper, zero changes
//   4. readMetricFile()   KEPT AS-IS — bufio.Scanner + parseMetricLine, zero changes
//   5. parseMetricLine()  KEPT AS-IS — strings.SplitN colon parser, zero changes
//   6. logInfo/Warning/fatalError  KEPT AS-IS — non-variadic string arg versions
//
//   7. writeCSV()  REMOVED — CSV to stdout
//      REPLACED BY writeStatsJSON() — writes data/stats.json for portfolio dashboard
//
//   8. loadJSON()  NEW — generic JSON file loader with graceful fallback
//      Missing or unreadable file → returns false, caller uses zero values
//
//   9. aggregateStats()  NEW — reads all four pipeline JSON files, builds DashboardStats
//      Each input is optional — missing file means zero/unknown for that section
//      Derives: attack counts, severity breakdown, top TTPs, FP rate, country count
//
//  10. main()  REWORKED
//      REMOVED: --input-glob (key:value text metric files as primary input)
//      ADDED:   --ir-cases, --fp-filter, --threat-ips, --posture, --output
//      KEPT:    --extra-metrics glob for custom key:value files (original flow preserved)
//      KEPT:    -v/--verbose unchanged
//
// ROLE IN THIR PIPELINE:
//   Reads outputs of Tools 26, 27, 29, 05 from data/ directory.
//   Aggregates into a single DashboardStats object.
//   Writes data/stats.json → portfolio metrics bar and posture dashboard reads it live.
//
// GITHUB ACTIONS USAGE:
//   go run tools/30_metric_exporter_live.go \
//     --ir-cases   data/ir_cases.json   \
//     --fp-filter  data/fp_filter.json  \
//     --threat-ips data/threat_ips.json \
//     --posture    data/posture.json    \
//     --output     data/stats.json
//
// OUTPUT FORMAT (data/stats.json):
//   {
//     "generated_at":      "2025-01-15T11:00:10Z",
//     "total_attacks":      47,
//     "unique_ips":         31,
//     "confirmed_threats":  38,
//     "false_positives":     9,
//     "fp_rate":            0.19,
//     "high_severity":      12,
//     "medium_severity":    18,
//     "low_severity":       17,
//     "total_ttps":          8,
//     "top_ttps":           [{"ttp":"T1110.001","count":67},{"ttp":"T1078","count":44},...],
//     "honeypot_status":   "UP",
//     "integrity_status":  "OK",
//     "unique_countries":   14,
//     "metrics":           [{"source":"custom","name":"patch_compliance","value":"94%",...}]
//   }

package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"time"
)

// -----------------------------------------------------------------------
// Structs
// -----------------------------------------------------------------------

// Metric represents a single parsed metric entry.
// Original Source/Name/Value fields preserved.
// ValueInt, ValueFloat, Category added for typed dashboard consumption.
type Metric struct {
	Source     string  `json:"source"`
	Name       string  `json:"name"`
	Value      string  `json:"value"`
	ValueInt   int     `json:"value_int,omitempty"`
	ValueFloat float64 `json:"value_float,omitempty"`
	Category   string  `json:"category,omitempty"`
}

// DashboardStats is the aggregated JSON written to data/stats.json.
// Pulls from all four pipeline tool outputs.
type DashboardStats struct {
	GeneratedAt      string   `json:"generated_at"`
	TotalAttacks     int      `json:"total_attacks"`
	UniqueIPs        int      `json:"unique_ips"`
	ConfirmedThreats int      `json:"confirmed_threats"`
	FalsePositives   int      `json:"false_positives"`
	FPRate           float64  `json:"fp_rate"`
	HighSeverity     int      `json:"high_severity"`
	MediumSeverity   int      `json:"medium_severity"`
	LowSeverity      int      `json:"low_severity"`
	TotalTTPs        int      `json:"total_ttps"`
	TopTTPs          []TTPStat `json:"top_ttps"`
	HoneypotStatus   string   `json:"honeypot_status"`
	IntegrityStatus  string   `json:"integrity_status"`
	UniqueCountries  int      `json:"unique_countries"`
	Metrics          []Metric `json:"metrics,omitempty"`
}

// TTPStat holds a TTP ID and its observed frequency.
type TTPStat struct {
	TTP   string `json:"ttp"`
	Count int    `json:"count"`
}

// -----------------------------------------------------------------------
// Logging helpers (unchanged from original — non-variadic string versions)
// -----------------------------------------------------------------------

var verbose bool

func logInfo(message string) {
	if verbose {
		fmt.Fprintln(os.Stderr, "[INFO]", message)
	}
}

func logWarning(message string) {
	fmt.Fprintln(os.Stderr, "[WARNING]", message)
}

func fatalError(message string) {
	fmt.Fprintln(os.Stderr, "[ERROR]", message)
	os.Exit(1)
}

// -----------------------------------------------------------------------
// File discovery and key:value metric parsing (unchanged from original)
// -----------------------------------------------------------------------

// discoverFiles finds files using a glob pattern.
// UNCHANGED from original.
func discoverFiles(pattern string) ([]string, error) {
	files, err := filepath.Glob(pattern)
	if err != nil {
		return nil, fmt.Errorf("failed to evaluate glob pattern: %v", err)
	}
	return files, nil
}

// readMetricFile reads and parses a single key:value metric file.
// UNCHANGED from original.
func readMetricFile(path string) ([]Metric, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, fmt.Errorf("failed to open file %s: %v", path, err)
	}
	defer file.Close()

	source := strings.TrimSuffix(filepath.Base(path), filepath.Ext(path))
	scanner := bufio.NewScanner(file)

	var metrics []Metric
	lineNumber := 0

	for scanner.Scan() {
		lineNumber++
		line := strings.TrimSpace(scanner.Text())

		if line == "" {
			continue
		}

		name, value, ok := parseMetricLine(line)
		if !ok {
			logWarning(fmt.Sprintf("malformed line %d in %s: %q", lineNumber, path, line))
			continue
		}

		metrics = append(metrics, Metric{
			Source: source,
			Name:   name,
			Value:  value,
		})
	}

	if err := scanner.Err(); err != nil {
		return metrics, fmt.Errorf("error reading file %s: %v", path, err)
	}

	return metrics, nil
}

// parseMetricLine parses "metric_name:metric_value" lines safely.
// UNCHANGED from original.
func parseMetricLine(line string) (string, string, bool) {
	parts := strings.SplitN(line, ":", 2)
	if len(parts) != 2 {
		return "", "", false
	}

	name := strings.TrimSpace(parts[0])
	value := strings.TrimSpace(parts[1])

	if name == "" || value == "" {
		return "", "", false
	}

	return name, value, true
}

// -----------------------------------------------------------------------
// JSON loading (new)
// -----------------------------------------------------------------------

// loadJSON reads a JSON file into the provided target interface.
// Returns false if file is missing or unreadable — caller uses zero values.
// Graceful fallback design: no file = no crash, just missing metrics.
func loadJSON(path string, target interface{}) bool {
	if path == "" {
		return false
	}

	data, err := os.ReadFile(path)
	if err != nil {
		logWarning(fmt.Sprintf("could not read %s: %v — skipping", path, err))
		return false
	}

	if err := json.Unmarshal(data, target); err != nil {
		logWarning(fmt.Sprintf("could not parse %s: %v — skipping", path, err))
		return false
	}

	return true
}

// -----------------------------------------------------------------------
// Stats aggregation (new)
// -----------------------------------------------------------------------

// aggregateStats reads all four pipeline JSON files and assembles DashboardStats.
// Each file is optional — missing file → zero/unknown for that section.
func aggregateStats(
	irCasesPath  string,
	fpFilterPath string,
	threatIPsPath string,
	posturePath  string,
	extraMetrics []Metric,
) DashboardStats {

	stats := DashboardStats{
		GeneratedAt:     time.Now().UTC().Format(time.RFC3339),
		HoneypotStatus:  "UNKNOWN",
		IntegrityStatus: "UNKNOWN",
		TopTTPs:         []TTPStat{},
		Metrics:         extraMetrics,
	}

	// ── Tool 26: ir_cases.json ──────────────────────────────────────────
	var irData struct {
		TotalCases int `json:"total_cases"`
		Cases      []struct {
			SrcIP    string   `json:"src_ip"`
			Severity string   `json:"severity"`
			TTPs     []string `json:"ttps"`
		} `json:"cases"`
	}

	if loadJSON(irCasesPath, &irData) {
		logInfo(fmt.Sprintf("loaded ir_cases: %d case(s)", irData.TotalCases))

		stats.TotalAttacks = irData.TotalCases

		// Unique IPs
		ipSeen := make(map[string]bool)
		// TTP frequency count
		ttpCount := make(map[string]int)

		for _, c := range irData.Cases {
			if c.SrcIP != "" {
				ipSeen[c.SrcIP] = true
			}
			switch strings.ToUpper(c.Severity) {
			case "HIGH":
				stats.HighSeverity++
			case "MEDIUM":
				stats.MediumSeverity++
			case "LOW":
				stats.LowSeverity++
			}
			for _, ttp := range c.TTPs {
				ttpCount[ttp]++
			}
		}

		stats.UniqueIPs = len(ipSeen)
		stats.TotalTTPs = len(ttpCount)

		// Top 5 TTPs by frequency
		type ttpFreq struct {
			TTP   string
			Count int
		}
		var freqs []ttpFreq
		for ttp, cnt := range ttpCount {
			freqs = append(freqs, ttpFreq{ttp, cnt})
		}
		sort.Slice(freqs, func(i, j int) bool {
			return freqs[i].Count > freqs[j].Count
		})
		limit := 5
		if len(freqs) < limit {
			limit = len(freqs)
		}
		for _, f := range freqs[:limit] {
			stats.TopTTPs = append(stats.TopTTPs, TTPStat{TTP: f.TTP, Count: f.Count})
		}
	} else {
		logWarning("ir_cases.json not loaded — attack metrics will be zero")
	}

	// ── Tool 29: fp_filter.json ─────────────────────────────────────────
	var fpData struct {
		ConfirmedThreats int     `json:"confirmed_threats"`
		FlaggedAsFP      int     `json:"flagged_as_fp"`
		FPRate           float64 `json:"fp_rate"`
	}

	if loadJSON(fpFilterPath, &fpData) {
		logInfo(fmt.Sprintf("loaded fp_filter: %d confirmed, %d FP", fpData.ConfirmedThreats, fpData.FlaggedAsFP))
		stats.ConfirmedThreats = fpData.ConfirmedThreats
		stats.FalsePositives = fpData.FlaggedAsFP
		stats.FPRate = fpData.FPRate
	} else {
		logWarning("fp_filter.json not loaded — FP metrics will be zero")
	}

	// ── Tool 27: threat_ips.json ────────────────────────────────────────
	var threatData struct {
		IPs []struct {
			Country string `json:"country"`
		} `json:"ips"`
	}

	if loadJSON(threatIPsPath, &threatData) {
		logInfo(fmt.Sprintf("loaded threat_ips: %d IP(s)", len(threatData.IPs)))
		countrySeen := make(map[string]bool)
		for _, ip := range threatData.IPs {
			if ip.Country != "" {
				countrySeen[ip.Country] = true
			}
		}
		stats.UniqueCountries = len(countrySeen)
	} else {
		logWarning("threat_ips.json not loaded — country count will be zero")
	}

	// ── Tool 05: posture.json ───────────────────────────────────────────
	var postureData struct {
		Summary struct {
			Overall string `json:"overall"`
		} `json:"summary"`
		IntegrityStatus string `json:"integrity_status,omitempty"`
	}

	if loadJSON(posturePath, &postureData) {
		logInfo(fmt.Sprintf("loaded posture: %s", postureData.Summary.Overall))
		if postureData.Summary.Overall != "" {
			stats.HoneypotStatus = postureData.Summary.Overall
		}
		if postureData.IntegrityStatus != "" {
			stats.IntegrityStatus = postureData.IntegrityStatus
		}
	} else {
		logWarning("posture.json not loaded — honeypot status will be UNKNOWN")
	}

	return stats
}

// -----------------------------------------------------------------------
// JSON output (replaces writeCSV)
// -----------------------------------------------------------------------

// writeStatsJSON writes DashboardStats to data/stats.json.
// Replaces writeCSV() — same role, JSON output for portfolio dashboard.
func writeStatsJSON(stats DashboardStats, outputPath string) error {
	data, err := json.MarshalIndent(stats, "", "  ")
	if err != nil {
		return fmt.Errorf("failed to marshal stats JSON: %v", err)
	}

	if err := os.WriteFile(outputPath, data, 0644); err != nil {
		return fmt.Errorf("failed to write %s: %v", outputPath, err)
	}

	return nil
}

// -----------------------------------------------------------------------
// Main entry point
// -----------------------------------------------------------------------

func main() {
	// Pipeline data file flags (new)
	irCasesPath  := flag.String("ir-cases",   "", "Path to data/ir_cases.json (Tool 26 output)")
	fpFilterPath := flag.String("fp-filter",  "", "Path to data/fp_filter.json (Tool 29 output)")
	threatIPsPath := flag.String("threat-ips", "", "Path to data/threat_ips.json (Tool 27 output)")
	posturePath  := flag.String("posture",    "", "Path to data/posture.json (Tool 05 output)")
	outputPath   := flag.String("output",     "data/stats.json", "Path to write stats.json")

	// Optional extra metrics glob — preserves original key:value file support
	extraMetricsGlob := flag.String("extra-metrics", "", `Glob for custom key:value metric files (e.g., "metrics/*.txt")`)

	// Verbose flag — unchanged from original
	flag.BoolVar(&verbose, "verbose", false, "Enable verbose output")
	flag.BoolVar(&verbose, "v", false, "Enable verbose output (shorthand)")
	flag.Parse()

	logInfo("starting Security Metric Dashboard Exporter (Live)")

	// ---- Optional: load extra key:value metric files (original flow preserved) ----
	var extraMetrics []Metric
	if strings.TrimSpace(*extraMetricsGlob) != "" {
		files, err := discoverFiles(*extraMetricsGlob)
		if err != nil {
			logWarning(fmt.Sprintf("extra-metrics glob error: %v", err))
		} else {
			logInfo(fmt.Sprintf("found %d extra metric file(s)", len(files)))
			for _, filePath := range files {
				metrics, err := readMetricFile(filePath)
				if err != nil {
					logWarning(err.Error())
					continue
				}
				extraMetrics = append(extraMetrics, metrics...)
			}
			logInfo(fmt.Sprintf("loaded %d extra metric(s)", len(extraMetrics)))
		}
	}

	// ---- Aggregate stats from all pipeline outputs ----
	stats := aggregateStats(
		*irCasesPath,
		*fpFilterPath,
		*threatIPsPath,
		*posturePath,
		extraMetrics,
	)

	// ---- Write stats.json ----
	if err := writeStatsJSON(stats, *outputPath); err != nil {
		fatalError(err.Error())
	}

	logInfo(fmt.Sprintf("stats written to %s", *outputPath))
	logInfo("export completed successfully")
}
