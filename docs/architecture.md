# RFOF CodeQL Network - Architecture Documentation

## 1. Overview and Purpose

The **`rfof-codeql-network`** repository forms the central control, rule, and security backbone for the entire decentralized RFOF network. It decouples security-relevant analysis logic from actual application repositories and enforces global standards based on static code analysis (CodeQL).

---

## 2. Modular Architecture

The repository's structure is divided into four primary functional areas:

| Module | Directory | Purpose |
| --- | --- | --- |
| **CI/CD Workflows** | `.github/workflows/` | Provision of reusable GitHub Actions (`workflow_call`) to automatedly enforce security checks across all projects. |
| **CLI & Wrapper** | `cli/` | Universal command-line interface (`rfof-codeql.sh`) and central configuration (`codeql-cli-config.yml`) for local and server-based analyses. |
| **Query Packs** | `queries/` | Custom, language-specific security rules (Python, JavaScript/TypeScript) acting as global filters against insecure code patterns. |
| **Workspace & UI** | `vscode-extension/` | Local development environment and workspace configuration (`rfof.code-workspace`) for seamless integration of query packs into VS Code. |

---

## 3. Data and Analysis Flow

1. **Rule Definition:** All security-relevant queries and standards are maintained centrally in this repository (`rfof-codeql-network`).
2. **Automated Integration:** Application repositories (such as the Python monolith) integrate the global workflow via `workflow_call`.
3. **Execution:** Upon every push or pull request, the target repository pulls the current queries, creates an isolated CodeQL database, and executes the analysis.
4. **Forced Correction & Protection:** Any vulnerabilities or violations are immediately reported within the pull request, establishing an unbroken, tamper-proof security shield across the entire global network.
