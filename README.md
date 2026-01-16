# CodeGuardian: AI-Powered Codebase Documentation

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/your-username/codeguardian)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

> A command-line tool that maps and documents codebases of any size using parallel AI sub-agents.

## About The Project

CodeGuardian is designed to give developers a high-level overview of any new or existing codebase. It recursively scans a target directory, dispatches AI-powered analysis agents to each file, and generates a consolidated report of the project's structure, components, and complexity.

This tool helps in:
*   Quickly onboarding new developers.
*   Identifying key components and potential areas for refactoring.
*   Generating automatic documentation stubs.

## Features

*   **Parallel Analysis:** Utilizes multiple AI agents to process files concurrently, making it fast and efficient for large codebases.
*   **Extensible Agent System:** Easily extendable to support different types of analysis (e.g., security vulnerabilities, style-guide compliance, dependency checking).
*   **CLI Interface:** Simple and intuitive command-line for easy integration into your workflow.
*   **Platform Agnostic:** Built with Python, it runs on Windows, macOS, and Linux.

## Getting Started

### Prerequisites

*   Python 3.9 or later

### Installation

1.  Clone the repo
    ```sh
    git clone https://github.com/your-username/codeguardian.git
    ```
2.  Install the package
    ```sh
    cd codeguardian
    pip install .
    ```

### Usage

To analyze a codebase, run CodeGuardian and point it to the target directory:

```sh
codeguardian /path/to/your/project
```

## License

Distributed under the MIT License. See `LICENSE` for more information.