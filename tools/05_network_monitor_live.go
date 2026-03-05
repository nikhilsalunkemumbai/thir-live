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

ROLE IN THIR PIPELINE:
  Checks Cowrie honeypot port 2222 on Oracle VPS every hour.
  Writes data/posture.json → portfolio posture dashboard reads it live.

GITHUB ACTIONS USAGE:
  go run tools/05_network_monitor_live.go \
    -h $ORACLE_VPS_IP -p 2222 \
    --json -o data/posture.json
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
	timeoutSec  int
	verboseMode bool
	jsonMode    bool // NEW: write JSON output for portfolio pipeline
)

// ServiceCheckResult stores the result of a single service check.
// ErrorMsg is a string so it serialises cleanly to JSON.
type ServiceCheckResult struct {
	Address   string    `json:"address"`
	Status    string    `json:"status"`
	ErrorMsg  string    `json:"error,omitempty"`
	CheckedAt time.Time `json:"checked_at"`
	Error     error     `json:"-"` // kept for internal use, excluded from JSON
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

func init() {
	flag.StringVar(&host, "host", "", "Host IP address or hostname to monitor.")
	flag.StringVar(&host, "h", "", "Host IP address or hostname to monitor (shorthand).")
	flag.IntVar(&port, "port", 0, "Port number to monitor.")
	flag.IntVar(&port, "p", 0, "Port number to monitor (shorthand).")
	flag.StringVar(&inputFile, "input", "", "Path to a file containing services to monitor (host:port per line).")
	flag.StringVar(&inputFile, "i", "", "Path to services file (shorthand).")
	flag.StringVar(&outputFile, "output", "", "Path to save report. Prints to stdout if not provided.")
	flag.StringVar(&outputFile, "o", "", "Output file path (shorthand).")
	flag.IntVar(&timeoutSec, "timeout", 3, "Connection timeout in seconds.")
	flag.IntVar(&timeoutSec, "t", 3, "Connection timeout in seconds (shorthand).")
	flag.BoolVar(&verboseMode, "verbose", false, "Enable verbose output.")
	flag.BoolVar(&verboseMode, "v", false, "Enable verbose output (shorthand).")
	flag.BoolVar(&jsonMode, "json", false, "Write JSON output for THIR pipeline (posture dashboard).")

	flag.Usage = func() {
		fmt.Fprintf(os.Stderr, "Usage of %s:\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "  Monitors network services. With --json writes posture data for THIR portfolio.\n")
		fmt.Fprintf(os.Stderr, "  Example (pipeline): %s -h ORACLE_VPS_IP -p 2222 --json -o data/posture.json\n", os.Args[0])
		fmt.Fprintf(os.Stderr, "  Example (text):     %s -h 192.168.1.1 -p 80\n", os.Args[0])
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

// writeJSONReport — NEW: writes posture.json for the portfolio dashboard.
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

	// Open output destination
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

	// Write report in chosen format
	if jsonMode {
		if err := writeJSONReport(allResults, output); err != nil {
			fmt.Fprintln(os.Stderr, err)
			os.Exit(1)
		}
	} else {
		writeTextReport(allResults, output)
	}

	if verboseMode {
		fmt.Fprintln(os.Stderr, "[INFO] Monitoring complete.")
	}
	os.Exit(0)
}
