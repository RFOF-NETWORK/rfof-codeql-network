# RFOF CodeQL CLI Wrapper

This module provides the decentralized command-line interface (CLI) for the **RFOF Network**, enabling automated creation and analysis of CodeQL databases both locally and within CI/CD pipelines.

## Features

* **Local Database Creation:** Generates isolated CodeQL databases directly from the source code.
* **Automated Analysis:** Applies global RFOF security queries (`queries/`).
* **SARIF Export:** Generates standardized reports (`codeql-results.sarif`) for seamless evaluation.

---

## Usage

Run the script directly in your terminal and pass the desired programming language (default is `python`):

```bash
# Run analysis for Python
./cli/rfof-codeql.sh python

# Run analysis for JavaScript
./cli/rfof-codeql.sh javascript

```

---

## Configuration

Global search paths and exclusion patterns are defined centrally in `codeql-cli-config.yml`.

