import os
import asyncio
from .agent import analyze_file

# File extensions to look for
SUPPORTED_EXTENSIONS = {'.py', '.js', '.java', '.c', '.cpp', '.h', '.cs', '.go', '.rs', '.ts', '.html', '.css'}

async def map_codebase(path: str):
    """
    Finds all supported files in a directory and runs agents on them in parallel.
    """
    file_paths = []
    for root, _, files in os.walk(path):
        for file in files:
            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                file_paths.append(os.path.join(root, file))

    if not file_paths:
        print("No supported files found in the specified directory.")
        return []

    print(f"Found {len(file_paths)} files to analyze. Starting agents...")

    tasks = [analyze_file(fp) for fp in file_paths]
    results = await asyncio.gather(*tasks)

    return results
