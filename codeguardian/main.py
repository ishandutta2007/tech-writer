import argparse
import asyncio
import os
from .mapper import map_codebase

def print_report(results: list):
    """Prints a summary report from the analysis results."""
    if not results:
        return

    print("\n--- CodeGuardian Analysis Report ---")
    total_files = len(results)
    total_lines = 0
    total_functions = 0
    total_classes = 0
    error_files = 0

    for res in results:
        if res.get("error"):
            error_files += 1
        else:
            total_lines += res.get("line_count", 0)
            total_functions += res.get("function_count", 0)
            total_classes += res.get("class_count", 0)

    print(f"\nOverall Stats:")
    print(f"  - Total Files Analyzed: {total_files}")
    print(f"  - Total Lines of Code: {total_lines}")
    print(f"  - Total Functions Found: {total_functions}")
    print(f"  - Total Classes Found: {total_classes}")
    if error_files > 0:
        print(f"  - Files with Errors: {error_files}")

    print("\n--- End of Report ---")


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(description="CodeGuardian - AI Codebase Analyzer")
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="The path to the codebase directory to analyze. Defaults to the current directory."
    )
    args = parser.parse_args()

    target_path = os.path.abspath(args.path)

    if not os.path.isdir(target_path):
        print(f"Error: Path '{target_path}' is not a valid directory.")
        return

    print(f"Starting analysis for directory: {target_path}")
    
    # Run the async mapping function
    results = asyncio.run(map_codebase(target_path))
    
    print_report(results)

if __name__ == "__main__":
    main()
