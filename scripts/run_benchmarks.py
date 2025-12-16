#!/usr/bin/env python3
"""
Benchmark Runner for NEO Compute Benchmarks

Runs all relevant benchmarks and saves results in JSON format for later comparison.
"""

import subprocess
import json
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import argparse
import csv
from io import StringIO


class BenchmarkRunner:
    """Run compute benchmarks and collect results."""

    def __init__(self, benchmark_dir: Path, output_file: Path, iterations: int = 10):
        self.benchmark_dir = benchmark_dir
        self.output_file = output_file
        self.iterations = iterations
        self.results: Dict[str, Any] = {"metadata": {}, "benchmarks": {}}

        # Initialize metadata
        self._init_metadata()

    def _init_metadata(self):
        """Initialize metadata section."""
        self.results["metadata"] = {
            "timestamp": datetime.now().isoformat(),
            "iterations": self.iterations,
            "device_info": self._get_device_info(),
        }

        print(
            f"Device: {self.results['metadata']['device_info'].get('device_name', 'Unknown')}"
        )
        print(
            f"Driver: {self.results['metadata']['device_info'].get('driver_version', 'Unknown')}"
        )
        print(f"Iterations: {self.iterations}\n")

    def _get_device_info(self) -> Dict[str, str]:
        """Get device information from ze_info."""
        try:
            result = subprocess.run(
                ["ze_info", "--list"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            device_info = {}
            for line in result.stdout.splitlines():
                if "Device Name:" in line:
                    device_info["device_name"] = line.split(":", 1)[1].strip()
                elif "Driver Version:" in line:
                    device_info["driver_version"] = line.split(":", 1)[1].strip()

            return (
                device_info
                if device_info
                else {"device_name": "Unknown", "driver_version": "Unknown"}
            )
        except Exception:
            return {"device_name": "Unknown", "driver_version": "Unknown"}

    def run_benchmark(
        self, benchmark_name: str, test_filter: str, timeout: int = 120
    ) -> List[Dict[str, Any]]:
        """Run a single benchmark with filter and parse CSV output."""
        benchmark_path = self.benchmark_dir / benchmark_name

        cmd = [
            str(benchmark_path),
            f"--gtest_filter={test_filter}",
            f"--iterations={self.iterations}",
            "--csv",
            "--noHeaders",
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
            )

            if result.returncode != 0:
                print(
                    f"    Warning: {benchmark_name} exited with code {result.returncode}"
                )
                if result.stderr:
                    print(f"    Error: {result.stderr[:200]}")
                return []

            # Parse CSV output
            return self._parse_csv_output(result.stdout)

        except subprocess.TimeoutExpired:
            print(f"    Warning: {benchmark_name} timed out")
            return []
        except Exception as e:
            print(f"    Error running {benchmark_name}: {e}")
            return []

    def _parse_csv_output(self, csv_text: str) -> List[Dict[str, Any]]:
        """Parse CSV output from benchmark."""
        results = []

        # Find CSV section (starts after headers)
        lines = csv_text.splitlines()
        csv_start = -1

        for i, line in enumerate(lines):
            if line.startswith("TestCase,"):
                csv_start = i
                break

        if csv_start == -1:
            return []

        # Parse CSV
        csv_section = "\n".join(lines[csv_start:])
        reader = csv.DictReader(StringIO(csv_section))

        for row in reader:
            # Convert numeric fields
            parsed_row = {"TestCase": row.get("TestCase", "")}

            for key, value in row.items():
                if key == "TestCase":
                    continue

                # Try to convert to float
                try:
                    if value and (
                        isinstance(value, str)
                        and value.strip()
                        or not isinstance(value, str)
                    ):
                        # Handle percentage values
                        if isinstance(value, str) and "%" in value:
                            parsed_row[key] = value
                        elif isinstance(value, str):
                            parsed_row[key] = float(value)
                        else:
                            parsed_row[key] = value
                    else:
                        parsed_row[key] = None
                except (ValueError, AttributeError):
                    parsed_row[key] = value

            results.append(parsed_row)

        return results

    def run_all_benchmarks(self):
        """Run all configured benchmarks."""
        # Define benchmarks to run
        benchmark_configs = [
            # API Overhead benchmarks (most important)
            {
                "name": "api_overhead_benchmark_l0",
                "categories": {
                    "UsmMemoryAllocation": "Usm*MemoryAllocation*",
                    "ExecuteCommandList": "ExecuteCommandList*",
                    "AppendLaunchKernel": "AppendLaunchKernel*",
                    "CreateCommandList": "CreateCommandList*",
                    "CreateBuffer": "CreateBuffer*",
                    "EventCreation": "Event*Test/*",
                    "ModuleCreate": "ModuleCreateSpv*",
                    "DriverGet": "DriverGet*",
                },
            },
            # Memory benchmarks
            {
                "name": "memory_benchmark_l0",
                "categories": {
                    "CopyBuffer": "*CopyBuffer*",
                    "FillBuffer": "*Fill*",
                },
            },
            # GPU commands
            {
                "name": "gpu_cmds_benchmark_l0",
                "categories": {
                    "Walker": "*Walker*",
                    "Execution": "*Execution*",
                },
            },
        ]

        # Run each benchmark
        for config in benchmark_configs:
            benchmark_name = config["name"]

            if not (self.benchmark_dir / benchmark_name).exists():
                print(f"Skipping {benchmark_name} (not found)")
                continue

            print(f"\n{'=' * 80}")
            print(f"Running: {benchmark_name}")
            print(f"{'=' * 80}\n")

            for category, test_filter in config["categories"].items():
                category_key = f"{benchmark_name}/{category}"
                results = self.run_benchmark(benchmark_name, test_filter, timeout=120)

                if results:
                    self.results["benchmarks"][category_key] = results
                    print(f"  ✓ {category}: {len(results)} tests")
                else:
                    print(f"  ✗ {category}: No results")

                # Small delay between tests
                time.sleep(0.5)

        # Save results
        self.save_results()

    def save_results(self):
        """Save results to JSON file."""
        self.output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(str(self.output_file), "w") as f:
            json.dump(self.results, f, indent=2)

        print(f"\n{'=' * 80}")
        print(f"Results saved to: {self.output_file}")
        print(f"Total benchmark categories: {len(self.results['benchmarks'])}")
        total_tests = sum(len(v) for v in self.results["benchmarks"].values())
        print(f"Total tests run: {total_tests}")
        print(f"{'=' * 80}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Run NEO compute benchmarks and save results"
    )
    parser.add_argument(
        "--benchmark-dir",
        default="~/compute-benchmarks/build/bin",
        help="Path to benchmark binaries directory",
    )
    parser.add_argument("--output", "-o", required=True, help="Output JSON file path")
    parser.add_argument(
        "--iterations",
        "-i",
        type=int,
        default=10,
        help="Number of iterations per test (default: 10)",
    )

    args = parser.parse_args()

    # Expand paths
    benchmark_dir = Path(args.benchmark_dir).expanduser()
    output_file = Path(args.output).expanduser()

    if not benchmark_dir.exists():
        print(f"Error: Benchmark directory not found: {benchmark_dir}")
        sys.exit(1)

    # Run benchmarks
    runner = BenchmarkRunner(benchmark_dir, output_file, args.iterations)

    try:
        runner.run_all_benchmarks()
    except KeyboardInterrupt:
        print("\n\nBenchmark interrupted by user")
        print(f"Partial results saved to: {output_file}")
        runner.save_results()
        sys.exit(1)


if __name__ == "__main__":
    main()
