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

## How to run

> Commands assume you have Python installed and are running from the project root.

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies

```powershell
pip install -r requirements.txt
```

3. Create data/raw directory and upload the dataset there

4. Run the pipeline:

Using Snakefile from roots:

```powershell
snakemake -c1 -s workflows/Snakefile
```

## Data handling rules

-   Keep raw files unchanged in data/raw/.
-   Do not commit raw data to Git.

## Versioning and Releases

The final, graded submission of this project is tagged as **v1.0** in Git.
All results, documentation, and outputs in this repository are reproducible
from this tagged version.

Contact

Maintainer: M. R.
Date: 2026-01-04
