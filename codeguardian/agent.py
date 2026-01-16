import asyncio
import re

async def analyze_file(file_path: str) -> dict:
    """
    Simulates an AI agent analyzing a single file.

    For this basic version, it counts lines, and estimates function/class counts.
    """
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Simulate async work (like an API call)
        await asyncio.sleep(0.01)

        lines = content.splitlines()
        line_count = len(lines)

        # Basic regex to find Python/Java/JS-style functions and classes
        function_pattern = re.compile(r'^\s*(def|function|public|private|protected)\s+\w+')
        class_pattern = re.compile(r'^\s*class\s+\w+')

        function_count = sum(1 for line in lines if function_pattern.match(line))
        class_count = sum(1 for line in lines if class_pattern.match(line))

        return {
            "file_path": file_path,
            "line_count": line_count,
            "function_count": function_count,
            "class_count": class_count,
            "error": None
        }
    except Exception as e:
        return {
            "file_path": file_path,
            "error": str(e)
        }
