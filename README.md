# Github Workflow Lab — IE7374 MLOps Lab 3

A Python scientific calculator with automated CI/CD testing via GitHub Actions. The lab uses two testing frameworks (**pytest** and **unittest**) triggered through separate GitHub Actions workflows.

---

## Lab Structure

```
project_dir/
├── src/
│   ├── __init__.py
│   └── scientific_calc.py
├── test/
│   ├── __init__.py
│   ├── test_sci_pytest.py
│   └── test_sci_unittest.py
├── workflows/
│   ├── sci_pytest_workflow.yml
│   └── sci_unittest_workflow.yml
├── requirements.txt
└── README.md
```

---

## Functions Included

| Function | Description |
|---|---|
| `square_root(x)` | Square root of a non-negative number |
| `power(base, exponent)` | Raise base to a power |
| `logarithm(x, base)` | Logarithm with optional base (default: natural log) |
| `sine(angle_degrees)` | Sine of an angle in degrees |
| `cosine(angle_degrees)` | Cosine of an angle in degrees |
| `tangent(angle_degrees)` | Tangent of an angle in degrees |
| `factorial(n)` | Factorial of a non-negative integer |

---

## How to Run Locally

### Prerequisites

- Python 3.9 or higher
- pip

### Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd MLOpsLab3
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run pytest**
   ```bash
   pytest -v
   ```

5. **Run unittest**
   ```bash
   python -m unittest discover -s test -p "test_sci_unittest.py" -v
   ```

---

## How to Run the GitHub Actions Workflows

### Guide

1. **Copy workflow files into the correct directory**
   GitHub Actions looks for workflows inside `.github/workflows/`. Copy (or move) the YAML files (ignore if they already exist):
   ```bash
   mkdir -p .github/workflows
   cp workflows/sci_pytest_workflow.yml .github/workflows/
   cp workflows/sci_unittest_workflow.yml .github/workflows/
   ```

2. **Push the repository to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - scientific calculator with CI"
   git branch -M main
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

3. **Workflows trigger automatically**
   - **Pytest workflow** triggers on pushes to `main` or `feature/**` branches, and on pull requests to `main`. It also runs when changes are made to `src/`, `test/`, or `requirements.txt`.
   - **Unittest workflow** triggers on pushes to `main` or `hotfix/**` branches, on pull requests to `main`, and on a weekly schedule (every Monday at 6 AM UTC).

4. **Trigger a workflow manually (Pytest only)**
   - Go to your GitHub repo → **Actions** tab → select **Scientific Calculator - Pytest Suite** → click **Run workflow**.
   - Choose the verbosity level (`-v`, `-vv`, or `-q`) and click **Run workflow**.

5. **View results**
   - Go to the **Actions** tab on your GitHub repository.
   - Click on the latest workflow run to see the logs for each Python version (3.9, 3.10, 3.11).
   - For the pytest workflow, download the test results XML artifact from the run summary.

---

## GitHub Actions Workflows

- The **workflow** is defined in a YAML file inside `.github/workflows/`.
- Each workflow contains **triggers** (`on:`) and **jobs**.
- Each job has a series of **steps** that run commands or use pre-built actions.

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```
This means the workflow runs when code is pushed to `main` or when a pull request targets `main`.

Other triggers used in this lab :
- `paths:` — only run if specific files changed
- `workflow_dispatch:` — allows manual triggering from the GitHub UI
- `schedule:` — run on a cron schedule

```yaml
strategy:
  matrix:
    python-version: ['3.9', '3.10', '3.11']
```
This runs the same job three times, once for each Python version. It helps verify compatibility.

| Step | Purpose |
|---|---|
| `actions/checkout@v4` | Clones your repo into the runner |
| `actions/setup-python@v5` | Installs the specified Python version |
| `actions/cache@v4` | Caches pip packages |
| `pip install -r requirements.txt` | Installs lab dependencies |
| `pytest ...` or `python -m unittest ...` | Runs the test suite |
| `actions/upload-artifact@v4` | Saves test reports as downloadable artifacts |

```yaml
- name: Print success banner
  if: success()
  run: echo "All tests passed"
```
- `if: success()` — runs only if all previous steps passed.
- `if: failure()` — runs only if a previous step failed.
- `if: always()` — runs regardless of outcome (useful for uploading artifacts).

1. Make a small change to `src/scientific_calc.py` (e.g., break a function on purpose).
2. Push the change and watch the workflow fail.
3. Fix the function, push again, and watch it pass.
4. Try creating a feature branch (`feature/my-test`) and push to it, observe the pytest workflow triggers.
5. Open a pull request and see both workflows run.

---

## Requirements

- `pytest` — for the pytest test suite

---