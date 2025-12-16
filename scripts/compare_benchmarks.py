#!/usr/bin/env python3
"""
Benchmark Comparison Report Generator

Compares two benchmark result files and generates a detailed analysis report.
"""

import json
import argparse
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple, Optional
from collections import defaultdict
import re


class BenchmarkComparator:
    """Compare two benchmark result sets."""

    def __init__(
        self,
        baseline_file: Path,
        comparison_file: Path,
        output_file: Optional[Path] = None,
    ):
        self.baseline_file = baseline_file
        self.comparison_file = comparison_file
        self.output_file = output_file

        self.baseline_data: Dict[str, Any] = {}
        self.comparison_data: Dict[str, Any] = {}
        self.report_lines: List[str] = []

    def load_data(self):
        """Load both benchmark result files."""
        try:
            with open(str(self.baseline_file), "r") as f:
                self.baseline_data = json.load(f)
        except Exception as e:
            print(f"Error loading baseline file: {e}")
            sys.exit(1)

        try:
            with open(str(self.comparison_file), "r") as f:
                self.comparison_data = json.load(f)
        except Exception as e:
            print(f"Error loading comparison file: {e}")
            sys.exit(1)

    def parse_stddev(self, stddev_str: str) -> float:
        """Parse StdDev string like '23.49%' to float."""
        if not stddev_str:
            return 0.0
        match = re.search(r"([\d.]+)%?", stddev_str)
        if match:
            return float(match.group(1))
        return 0.0

    def calculate_improvement(
        self, baseline_val: float, comparison_val: float
    ) -> Tuple[float, str]:
        """Calculate percentage improvement (negative means regression)."""
        if baseline_val == 0:
            return 0.0, "N/A"

        improvement = ((baseline_val - comparison_val) / baseline_val) * 100

        if abs(improvement) < 1:
            emoji = "≈"  # negligible
        elif improvement > 0:
            if improvement > 20:
                emoji = "🚀"  # massive improvement
            elif improvement > 10:
                emoji = "✅"  # significant improvement
            else:
                emoji = "✓"  # minor improvement
        else:
            if improvement < -20:
                emoji = "🔴"  # massive regression
            elif improvement < -10:
                emoji = "⚠️"  # significant regression
            else:
                emoji = "↓"  # minor regression

        return improvement, emoji

    def find_matching_test(
        self, test_case: str, test_list: List[Dict]
    ) -> Optional[Dict]:
        """Find matching test case in list."""
        for test in test_list:
            if test["TestCase"] == test_case:
                return test
        return None

    def write(self, line: str = ""):
        """Add line to report."""
        self.report_lines.append(line)

    def generate_header(self):
        """Generate report header."""
        baseline_meta = self.baseline_data.get("metadata", {})
        comparison_meta = self.comparison_data.get("metadata", {})

        self.write("# Benchmark Comparison Report")
        self.write()
        self.write("## Configuration")
        self.write()
        self.write("### Baseline")
        self.write(f"- **File**: `{self.baseline_file.name}`")
        self.write(f"- **Timestamp**: {baseline_meta.get('timestamp', 'Unknown')}")
        self.write(
            f"- **Device**: {baseline_meta.get('device_info', {}).get('device_name', 'Unknown')}"
        )
        self.write(
            f"- **Driver**: {baseline_meta.get('device_info', {}).get('driver_version', 'Unknown')}"
        )
        self.write(f"- **Iterations**: {baseline_meta.get('iterations', 'Unknown')}")
        self.write()

        self.write("### Comparison")
        self.write(f"- **File**: `{self.comparison_file.name}`")
        self.write(f"- **Timestamp**: {comparison_meta.get('timestamp', 'Unknown')}")
        self.write(
            f"- **Device**: {comparison_meta.get('device_info', {}).get('device_name', 'Unknown')}"
        )
        self.write(
            f"- **Driver**: {comparison_meta.get('device_info', {}).get('driver_version', 'Unknown')}"
        )
        self.write(f"- **Iterations**: {comparison_meta.get('iterations', 'Unknown')}")
        self.write()
        self.write("---")
        self.write()

    def generate_summary(self, category_stats: Dict):
        """Generate executive summary."""
        self.write("## Executive Summary")
        self.write()

        # Calculate overall statistics
        all_improvements = []
        significant_improvements = []
        significant_regressions = []

        for category, stats in category_stats.items():
            all_improvements.extend(stats["improvements"])

            for imp, test_name in stats["median_improvements"]:
                if imp > 10:
                    significant_improvements.append((imp, test_name, category))
                elif imp < -10:
                    significant_regressions.append((imp, test_name, category))

        if all_improvements:
            avg_improvement = sum(all_improvements) / len(all_improvements)

            self.write(f"**Overall Performance Change**: {avg_improvement:+.1f}%")
            self.write()

            if significant_improvements:
                self.write(
                    f"### 🚀 Top Improvements ({len(significant_improvements)} tests >10% faster)"
                )
                self.write()

                # Sort by improvement (highest first)
                significant_improvements.sort(reverse=True)

                for imp, test_name, category in significant_improvements[:10]:
                    self.write(f"- **{imp:+.1f}%** - {test_name} ({category})")

                self.write()

            if significant_regressions:
                self.write(
                    f"### ⚠️ Regressions ({len(significant_regressions)} tests >10% slower)"
                )
                self.write()

                # Sort by regression (worst first)
                significant_regressions.sort()

                for imp, test_name, category in significant_regressions[:10]:
                    self.write(f"- **{imp:+.1f}%** - {test_name} ({category})")

                self.write()

        self.write("---")
        self.write()

    def generate_category_report(
        self, category: str, baseline_tests: List[Dict], comparison_tests: List[Dict]
    ) -> Dict:
        """Generate detailed report for a category."""

        self.write(f"## {category}")
        self.write()

        # Match tests and calculate stats
        matched_tests = []
        stats = {
            "improvements": [],
            "median_improvements": [],
        }

        for baseline_test in baseline_tests:
            test_case = baseline_test["TestCase"]
            comparison_test = self.find_matching_test(test_case, comparison_tests)

            if comparison_test:
                matched_tests.append(
                    {
                        "name": test_case,
                        "baseline": baseline_test,
                        "comparison": comparison_test,
                    }
                )

                # Calculate improvement based on median (more stable than mean)
                if baseline_test["Median"] and comparison_test["Median"]:
                    improvement, _ = self.calculate_improvement(
                        baseline_test["Median"], comparison_test["Median"]
                    )
                    stats["improvements"].append(improvement)
                    stats["median_improvements"].append((improvement, test_case))

        if not matched_tests:
            self.write("*No matching tests found*")
            self.write()
            return stats

        # Sort by improvement
        matched_tests.sort(
            key=lambda x: (
                self.calculate_improvement(
                    x["baseline"]["Median"] or 0, x["comparison"]["Median"] or 0
                )[0]
            ),
            reverse=True,
        )

        # Generate table
        self.write(
            "| Test | Baseline (Median) | Comparison (Median) | Change | Status |"
        )
        self.write(
            "|------|-------------------|---------------------|--------|--------|"
        )

        for test in matched_tests:
            name = test["name"]
            baseline_median = test["baseline"]["Median"]
            comparison_median = test["comparison"]["Median"]

            if baseline_median is None or comparison_median is None:
                continue

            improvement, emoji = self.calculate_improvement(
                baseline_median, comparison_median
            )

            # Shorten test name if too long
            display_name = name
            if len(name) > 60:
                display_name = name[:57] + "..."

            self.write(
                f"| {display_name} | "
                f"{baseline_median:.3f} µs | "
                f"{comparison_median:.3f} µs | "
                f"{improvement:+.1f}% | "
                f"{emoji} |"
            )

        self.write()

        # Category statistics
        if stats["improvements"]:
            avg_improvement = sum(stats["improvements"]) / len(stats["improvements"])
            self.write(f"**Category Average**: {avg_improvement:+.1f}% change")
            self.write()

        return stats

    def generate_report(self):
        """Generate full comparison report."""
        self.load_data()

        self.generate_header()

        # Process each category
        baseline_benchmarks = self.baseline_data.get("benchmarks", {})
        comparison_benchmarks = self.comparison_data.get("benchmarks", {})

        # Find common categories
        common_categories = set(baseline_benchmarks.keys()) & set(
            comparison_benchmarks.keys()
        )

        if not common_categories:
            self.write("**ERROR**: No common benchmark categories found!")
            return

        # Collect stats for summary
        all_category_stats = {}

        # Generate detailed reports for each category
        for category in sorted(common_categories):
            baseline_tests = baseline_benchmarks[category]
            comparison_tests = comparison_benchmarks[category]

            stats = self.generate_category_report(
                category, baseline_tests, comparison_tests
            )
            all_category_stats[category] = stats

            self.write("---")
            self.write()

        # Insert summary at the beginning (after header)
        header_lines = []
        detail_lines = []
        in_header = True

        for line in self.report_lines:
            if line == "---" and in_header:
                in_header = False
                header_lines.append(line)
                header_lines.append("")
                continue

            if in_header:
                header_lines.append(line)
            else:
                detail_lines.append(line)

        # Regenerate with summary
        self.report_lines = header_lines
        self.generate_summary(all_category_stats)
        self.report_lines.extend(detail_lines)

    def save_report(self):
        """Save report to file or print to stdout."""
        report_text = "\n".join(self.report_lines)

        if self.output_file:
            self.output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(str(self.output_file), "w") as f:
                f.write(report_text)
            print(f"Report saved to: {self.output_file}")
        else:
            print(report_text)


def main():
    parser = argparse.ArgumentParser(
        description="Compare two benchmark result files and generate a report"
    )
    parser.add_argument("baseline", help="Baseline benchmark results (JSON file)")
    parser.add_argument("comparison", help="Comparison benchmark results (JSON file)")
    parser.add_argument(
        "--output",
        "-o",
        help="Output report file (markdown). If not specified, prints to stdout.",
    )

    args = parser.parse_args()

    # Expand paths
    baseline_file = Path(args.baseline).expanduser()
    comparison_file = Path(args.comparison).expanduser()
    output_file = Path(args.output).expanduser() if args.output else None

    if not baseline_file.exists():
        print(f"Error: Baseline file not found: {baseline_file}")
        sys.exit(1)

    if not comparison_file.exists():
        print(f"Error: Comparison file not found: {comparison_file}")
        sys.exit(1)

    # Generate comparison
    comparator = BenchmarkComparator(baseline_file, comparison_file, output_file)
    comparator.generate_report()
    comparator.save_report()


if __name__ == "__main__":
    main()
