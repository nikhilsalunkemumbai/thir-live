/*
THIR LIVE PIPELINE — PRODUCTION TOOL
Adapted from: CybersecurityPortfolio/05_network_service_monitor.go

CHANGES FROM ORIGINAL:
  1. Added JSON output mode (encoding/json import)
  2. Added --json flag to write machine-readable posture data
  3. Added CheckedAt timestamp to results
  4. Added ErrorMsg string field (JSON-serialisable, Error interface is not)
  5. writeJSONReport() replaces writeReport() when --json flag is set
  6. All original CLI flags and text-report behaviour preserved

v2 ADDITIONS (ID.AM-1 — Asset Inventory):
  7. Added --assets flag to write data/assets.json alongside posture.json
  8. AssetRecord struct covers: asset_id, hostname, ip, port, role,
     classification, owner, status, first_seen, last_seen
  9. writeAssetsJSON() writes the asset register
 10. Assets file is append-aware: if assets.json exists, first_seen is
     preserved from the existing record so asset age is tracked correctly

NIST CSF COVERAGE:
  posture.json → DE.CM-1  (Honeypot Liveness Monitoring)
  assets.json  → ID.AM-1  (Asset Inventory)

ROLE IN THIR PIPELINE:
  Checks Cowrie honeypot port 2222 on AWS EC2 every hour.
  Writes data/posture.json → portfolio posture dashboard reads it live.
  Writes data/assets.json  → asset inventory for ID.AM-1 coverage.

GITHUB ACTIONS USAGE:
  go run tools/05_network_monitor_live.go \
    -h $ORACLE_VPS_IP -p 2222 \
    --json -o data/posture.json \
    --assets data/assets.json \
    -v
*/

package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"net"
	"os"
	"strings"
	"time"
)

// Global variables for CLI flags
var (
	host        string
	port        int
	inputFile   string
	outputFile  string
	assetsFile  string // NEW: path for assets.json
	timeoutSec  int
	verboseMode bool
	jsonMode    bool
)

// ServiceCheckResult stores the result of a single service check.
type ServiceCheckResult struct {
	Address   string    `json:"address"`
	Status    string    `json:"status"`
	ErrorMsg  string    `json:"error,omitempty"`
	CheckedAt time.Time `json:"checked_at"`
	Error     error     `json:"-"`
}

// PostureReport is the JSON structure written to data/posture.json
type PostureReport struct {
	GeneratedAt time.Time            `json:"generated_at"`
	Services    []ServiceCheckResult `json:"services"`
	Summary     PostureSummary       `json:"summary"`
}

type PostureSummary struct {
	Total   int    `json:"total"`
	Up      int    `json:"up"`
	Down    int    `json:"down"`
	Overall string `json:"overall"` // "HEALTHY" | "DEGRADED" | "DOWN"
}

// AssetRecord represents a single known asset in the inventory.
// Covers NIST CSF ID.AM-1: Physical devices and systems are inventoried.
type AssetRecord struct {
	AssetID        string    `json:"asset_id"`        // stable identifier, e.g. "thir-honeypot-01"
	Hostname       string    `json:"hostname"`        // DNS name or label
	IPAddress      string    `json:"ip_address"`      // observed IP
	Port           int       `json:"port"`            // monitored port
	Role           string    `json:"role"`            // e.g. "Cowrie SSH Honeypot"
	Classification string    `json:"classification"`  // "PUBLIC" | "INTERNAL" | "SENSITIVE"
	Owner          string    `json:"owner"`           // asset owner / operator
	Platform       string    `json:"platform"`        // "AWS EC2 Ubuntu"
	Status         string    `json:"status"`          // "UP" | "DOWN" | "UNKNOWN"
	FirstSeen      time.Time `json:"first_seen"`      // preserved across runs
	LastSeen       time.Time `json:"last_seen"`       // updated every run
	LastChecked    time.Time `json:"last_checked"`    // timestamp of this check
	NistControl    string    `json:"nist_control"`    // "ID.AM-1"
	NistFunction   string    `json:"nist_function"`   // "IDENTIFY"
}

// AssetInventory is the top-level structure for data/assets.json
type AssetInventory struct {
	GeneratedAt   time.Time     `json:"generated_at"`
	NistControl   string        `json:"nist_control"`   // "ID.AM-1"
	NistFunction  string        `json:"nist_function"`  // "IDENTIFY"
	Description   string        `json:"description"`
	TotalAssets   int           `json:"total_assets"`
	AssetsOnline  int           `json:"assets_online"`
	AssetsOffline int           `json:"assets_offline"`
	Assets        []AssetRecord `json:"assets"`
}

func init() {
	flag.StringVar(&host, "host", "", "Host IP address or hostname to monitor.")
	flag.StringVar(&host, "h", "", "Host IP address or hostname to monitor (shorthand).")
	flag.IntVar(&port, "port", 0, "Port number to monitor.")
	flag.IntVar(&port, "p", 0, "Port number to monitor (shorthand).")
	flag.StringVar(&inputFile, "input", "", "Path to a file containing services to monitor (host:port per line).")
	flag.StringVar(&inputFile, "i", "", "Path to services file (shorthand).")
	flag.StringVar(&outputFile, "output", "", "Path to save posture report. Prints to stdout if not provided.")
	flag.StringVar(&outputFile, "o", "", "Output file path (shorthand).")
	flag.StringVar(&assetsFile, "assets", "", "Path to write asset inventory JSON (data/assets.json). Enables ID.AM-1 coverage.")
	flag.IntVar(&timeoutSec, "timeout", 3, "Connection timeout in seconds.")
	flag.IntVar(&timeoutSec, "t", 3, "Connection timeout in seconds (shorthand).")
	flag.BoolVar(&verboseMode, "verbose", false, "Enable verbose output.")
	flag.BoolVar(&verboseMode, "v", false, "Enable verbose output (shorthand).")
	flag.BoolVar(&jsonMode, "json", false, "Write JSON output for THIR pipeline (posture dashboard).")

	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage of %s:\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "  Monitors network services. Writes posture + asset inventory for THIR pipeline.\n")
		fmt.Fprintf(os.Stderr, "  Example (pipeline):\n")
		fmt.Fprintf(os.Stderr, "    %s -h $VPS_IP -p 2222 --json -o data/posture.json --assets data/assets.json -v\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "  Example (text only):\n")
		fmt.Fprintf(os.Stderr, "    %s -h 192.168.1.1 -p 80\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "Flags:\n")
		flag.PrintDefaults()
	}
}

// checkService attempts TCP connection to the given address.
func checkService(address string, timeout time.Duration) ServiceCheckResult {
	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] Checking service: %s\n", address)
	}
	checkedAt := time.Now().UTC()
	conn, err := net.DialTimeout("tcp", address, timeout)
	if err != nil {
		return ServiceCheckResult{
			Address:   address,
			Status:    "DOWN",
			ErrorMsg:  err.Error(),
			Error:     err,
			CheckedAt: checkedAt,
		}
	}
	defer conn.Close()
	return ServiceCheckResult{
		Address:   address,
		Status:    "UP",
		CheckedAt: checkedAt,
	}
}

// loadServicesFromFile reads host:port pairs from a file.
func loadServicesFromFile(filePath string) ([]string, error) {
	file, err := os.Open(filePath)
	if err != nil {
		return nil, fmt.Errorf("[ERROR] Failed to open input file %s: %w", filePath, err)
	}
	defer file.Close()

	var services []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())
		if line != "" {
			services = append(services, line)
		}
	}
	if err := scanner.Err(); err != nil {
		return nil, fmt.Errorf("[ERROR] Error reading input file %s: %w", filePath, err)
	}
	return services, nil
}

// writeTextReport — original text report, preserved unchanged.
func writeTextReport(results []ServiceCheckResult, output *os.File) {
	fmt.Fprintf(output, "--- Network Service Monitor Report ---\n\n")
	if len(results) == 0 {
		fmt.Fprintln(output, "No services were monitored or no results to report.")
		return
	}
	for _, result := range results {
		fmt.Fprintf(output, "Service: %s\n", result.Address)
		fmt.Fprintf(output, "Status:  %s\n", result.Status)
		if result.ErrorMsg != "" {
			fmt.Fprintf(output, "Error:   %s\n", result.ErrorMsg)
		}
		fmt.Fprintln(output, "------------------------------")
	}
}

// writeJSONReport — writes posture.json for the portfolio dashboard.
func writeJSONReport(results []ServiceCheckResult, output *os.File) error {
	up, down := 0, 0
	for _, r := range results {
		if r.Status == "UP" {
			up++
		} else {
			down++
		}
	}

	overall := "HEALTHY"
	if down > 0 && up > 0 {
		overall = "DEGRADED"
	} else if down > 0 {
		overall = "DOWN"
	}

	report := PostureReport{
		GeneratedAt: time.Now().UTC(),
		Services:    results,
		Summary: PostureSummary{
			Total:   len(results),
			Up:      up,
			Down:    down,
			Overall: overall,
		},
	}

	enc := json.NewEncoder(output)
	enc.SetIndent("", "  ")
	if err := enc.Encode(report); err != nil {
		return fmt.Errorf("[ERROR] Failed to encode JSON: %w", err)
	}
	return nil
}

// loadExistingAssets reads the current assets.json to preserve first_seen timestamps.
// Returns a map of asset_id → AssetRecord. Returns empty map if file doesn't exist.
func loadExistingAssets(filePath string) map[string]AssetRecord {
	existing := make(map[string]AssetRecord)
	data, err := os.ReadFile(filePath)
	if err != nil {
		return existing // file doesn't exist yet — that's fine
	}
	var inv AssetInventory
	if err := json.Unmarshal(data, &inv); err != nil {
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[WARN] Could not parse existing assets.json: %v — will rebuild\n", err)
		}
		return existing
	}
	for _, a := range inv.Assets {
		existing[a.AssetID] = a
	}
	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] Loaded %d existing asset record(s) from %s\n", len(existing), filePath)
	}
	return existing
}

// buildAssetRecord constructs an AssetRecord from a ServiceCheckResult.
// Preserves first_seen from existing record if available.
func buildAssetRecord(result ServiceCheckResult, existing map[string]AssetRecord) AssetRecord {
	// Parse host and port from result.Address ("ip:port")
	h, p, err := net.SplitHostPort(result.Address)
	if err != nil {
		h = result.Address
		p = "0"
	}
	portNum := 0
	fmt.Sscanf(p, "%d", &portNum)

	assetID := fmt.Sprintf("thir-honeypot-%s-%s", h, p)

	now := time.Now().UTC()
	firstSeen := now

	// Preserve first_seen if this asset was seen before
	if prev, ok := existing[assetID]; ok {
		firstSeen = prev.FirstSeen
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[INFO] Asset %s: preserving first_seen = %s\n", assetID, firstSeen.Format(time.RFC3339))
		}
	} else {
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[INFO] Asset %s: new asset, setting first_seen = %s\n", assetID, firstSeen.Format(time.RFC3339))
		}
	}

	lastSeen := now
	if result.Status != "UP" {
		// Don't update last_seen if asset is down — preserve last known-good time
		if prev, ok := existing[assetID]; ok {
			lastSeen = prev.LastSeen
		}
	}

	return AssetRecord{
		AssetID:        assetID,
		Hostname:       h,
		IPAddress:      h,
		Port:           portNum,
		Role:           "Cowrie SSH Honeypot",
		Classification: "PUBLIC",
		Owner:          "Joy Dane — THIR Project",
		Platform:       "AWS EC2 Ubuntu",
		Status:         result.Status,
		FirstSeen:      firstSeen,
		LastSeen:       lastSeen,
		LastChecked:    now,
		NistControl:    "ID.AM-1",
		NistFunction:   "IDENTIFY",
	}
}

// writeAssetsJSON builds and writes data/assets.json. Covers NIST ID.AM-1.
func writeAssetsJSON(results []ServiceCheckResult, filePath string) error {
	existing := loadExistingAssets(filePath)

	var assets []AssetRecord
	online, offline := 0, 0

	for _, r := range results {
		asset := buildAssetRecord(r, existing)
		assets = append(assets, asset)
		if asset.Status == "UP" {
			online++
		} else {
			offline++
		}
	}

	inventory := AssetInventory{
		GeneratedAt:   time.Now().UTC(),
		NistControl:   "ID.AM-1",
		NistFunction:  "IDENTIFY",
		Description:   "Physical devices and systems within the THIR honeypot infrastructure are inventoried. Updated hourly by Tool 05.",
		TotalAssets:   len(assets),
		AssetsOnline:  online,
		AssetsOffline: offline,
		Assets:        assets,
	}

	data, err := json.MarshalIndent(inventory, "", "  ")
	if err != nil {
		return fmt.Errorf("[ERROR] Failed to marshal assets JSON: %w", err)
	}

	if err := os.WriteFile(filePath, data, 0644); err != nil {
		return fmt.Errorf("[ERROR] Failed to write assets file %s: %w", filePath, err)
	}

	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] Asset inventory written to %s (%d asset(s), %d online)\n",
			filePath, len(assets), online)
	}
	return nil
}

func main() {
	flag.Parse()

	if inputFile == "" && (host == "" || port == 0) {
		flag.Usage()
		fmt.Fprintln(os.Stderr, "\n[ERROR] Either an input file (-i) or a host (-h) and port (-p) must be provided.")
		os.Exit(1)
	}
	if inputFile != "" && (host != "" || port != 0) {
		fmt.Fprintln(os.Stderr, "[WARNING] Input file (-i) provided. -host and -port flags will be ignored.")
	}

	var servicesToMonitor []string
	if inputFile != "" {
		loaded, err := loadServicesFromFile(inputFile)
		if err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(1)
		}
		servicesToMonitor = loaded
	} else {
		servicesToMonitor = []string{net.JoinHostPort(host, fmt.Sprintf("%d", port))}
	}

	if verboseMode {
		fmt.Fprintf(os.Stderr, "[INFO] Monitoring %d service(s)...\n", len(servicesToMonitor))
	}

	results := make(chan ServiceCheckResult, len(servicesToMonitor))
	timeout := time.Duration(timeoutSec) * time.Second

	for _, svc := range servicesToMonitor {
		go func(s string) {
			results <- checkService(s, timeout)
		}(svc)
	}

	var allResults []ServiceCheckResult
	for range servicesToMonitor {
		allResults = append(allResults, <-results)
	}

	// ── Write posture.json (DE.CM-1) ──────────────────────────────────
	output := os.Stdout
	if outputFile != "" {
		var err error
		output, err = os.Create(outputFile)
		if err != nil {
			fmt.Fprintf(os.Stderr, "[ERROR] Failed to create output file %s: %v\n", outputFile, err)
			os.Exit(1)
		}
		defer output.Close()
	}

	if jsonMode {
		if err := writeJSONReport(allResults, output); err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(1)
		}
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[INFO] posture.json written (DE.CM-1)\n")
		}
	} else {
		writeTextReport(allResults, output)
	}

	// ── Write assets.json (ID.AM-1) ───────────────────────────────────
	if assetsFile != "" {
		if err := writeAssetsJSON(allResults, assetsFile); err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(1)
		}
		if verboseMode {
			fmt.Fprintf(os.Stderr, "[INFO] assets.json written (ID.AM-1)\n")
		}
	}

	if verboseMode {
		fmt.Fprintln(os.Stderr, "[INFO] Tool 05 complete.")
	}
	os.Exit(0)
}
