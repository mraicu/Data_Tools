# Reproducible Local Dataset Package

## Project Overview

This project provides a reproducible, research-grade data repository for an internal
records dataset covering years 2022 and 2023. The goal is to ensure that data cleaning,
validation, and analysis can be fully reproduced from a clean clone of the repository
using local data only, without external downloads.

The repository follows best practices for data versioning, documentation, and workflow
automation, and is intended for internal research or operational use.

## Folder Structure

-   `data/raw/`: Original datasets provided by the instructor (unchanged)
-   `data/interim/`: Optional intermediate files created during processing
-   `data/processed/`: Cleaned and harmonized datasets
-   `src/`: Python scripts for cleaning, validation, and analysis
-   `workflows/`: Reproducible pipeline (Makefile or Snakefile)
-   `docs/`: Dataset documentation (data dictionary, metadata)
-   `reports/`: Generated tables, figures, and short written report

## Reproducibility Instructions

1. Clone the repository locally.
2. Create the Python environment:
    ```bash
    pip install -r requirements.txt
    ```

Place the provided datasets into data/raw/.

Run the pipeline:

`make all`

## How to run

> Commands assume you have Python installed and are running from the project root.

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Run the pipeline (choose one workflow approach; you will implement in Task 6.5):

Using Make:

```powershell
make all
```

## Expected outputs

After running the pipeline, you should expect:

`data/processed/records_harmonized.csv`

-   Cleaned and harmonized records across 2022–2023.

`reports/summary_table.csv`

-   Basic counts by category/status/year, missingness stats, etc.

`reports/report.md`

-   Short reproducible report referencing the generated outputs.

## Data handling rules

-   Keep raw files unchanged in data/raw/.
-   Do not commit raw data to Git.

Contact

Maintainer: M. R.
Date: 2026-01-04
