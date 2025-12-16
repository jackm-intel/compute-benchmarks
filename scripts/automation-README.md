# Benchmark Automation Scripts

This directory contains scripts for automated benchmark execution and comparison, useful for performance regression testing and driver comparisons.

## Scripts

### `run_benchmarks.py`

Runs all relevant compute benchmarks and saves results to JSON format.

**Usage:**
```bash
# From the compute-benchmarks/scripts directory
cd scripts

# Run with default settings (10 iterations)
# Default benchmark dir is ~/compute-benchmarks/build/bin
./run_benchmarks.py -o baseline-results.json

# Run with custom iterations
./run_benchmarks.py \
  --iterations 100 \
  -o results.json

# Or specify a different benchmark directory
./run_benchmarks.py \
  --benchmark-dir ../build/bin \
  --iterations 100 \
  -o results.json
```

**Output:** JSON file containing:
- Metadata (timestamp, device info, driver version, iterations)
- Benchmark results organized by category
- Full CSV data (Mean, Median, Min, Max, StdDev)

**Benchmarks covered:**
- API Overhead: USM allocation, ExecuteCommandList, AppendLaunchKernel, CreateCommandList, etc.
- Memory: CopyBuffer, FillBuffer
- GPU Commands: Walker, Execution

### `compare_benchmarks.py`

Compares two benchmark result files and generates a detailed markdown report.

**Usage:**
```bash
# Print report to stdout
./compare_benchmarks.py baseline.json lazy-init.json

# Save report to file
./compare_benchmarks.py baseline.json lazy-init.json -o comparison-report.md
```

**Output:** Markdown report containing:
- Executive summary with overall performance change
- Top improvements and regressions
- Category-by-category detailed tables
- Visual indicators (🚀 massive improvement, ✅ significant, ⚠️ regression)

## Typical Workflow

### 1. Build benchmarks
```bash
cd compute-benchmarks
mkdir -p build && cd build
cmake ..
make -j$(nproc)
```

### 2. Baseline Measurement
```bash
cd ../scripts
# Make sure baseline driver is loaded
# Run baseline benchmarks
./run_benchmarks.py -o baseline-results.json --iterations 100
```

### 3. Test Build Measurement
```bash
# Load test driver (e.g., with your changes)
# Run same benchmarks
./run_benchmarks.py -o test-results.json --iterations 100
```

### 4. Generate Comparison
```bash
./compare_benchmarks.py baseline-results.json test-results.json \
  -o comparison-report.md
```

### 5. Review Results
```bash
# View the markdown report
cat comparison-report.md
# Or open in editor/browser
```

## Example Output

**run_benchmarks.py:**
```
Device: Intel(R) Arc(TM) B580 Graphics
Driver: 1.3.32231
Iterations: 100

================================================================================
Running: api_overhead_benchmark_l0
================================================================================

  ✓ UsmMemoryAllocation: 12 tests
  ✓ ExecuteCommandList: 8 tests
  ✓ AppendLaunchKernel: 15 tests
  ...

================================================================================
Results saved to: baseline-results.json
Total benchmark categories: 10
Total tests run: 157
================================================================================
```

**compare_benchmarks.py:**
```markdown
# Benchmark Comparison Report

## Executive Summary

**Overall Performance Change**: +47.3%

### 🚀 Top Improvements (42 tests >10% faster)

- **+65.2%** - AppendLaunchKernelAndMemcpy
- **+43.1%** - ExecuteCommandListImmediate
- **+38.7%** - UsmDeviceAllocationMultipleQueues
...
```

## Notes

- Scripts automatically detect device info using `ze_info --list`
- Results include full statistical data (not just mean/median)
- Comparison uses median values (more stable than mean)
- All paths support `~` expansion
- CSV parsing handles percentage fields (like StdDev) correctly
