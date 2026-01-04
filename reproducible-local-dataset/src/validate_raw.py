from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


EXPECTED_2022 = ["record_id", "date", "category", "value", "unit", "source", "status"]
EXPECTED_2023 = [
    "record_id",
    "date",
    "category",
    "value",
    "unit",
    "source_system",
    "status",
    "department",
    "priority",
]

ALLOWED_STATUS = {"ok", "cancelled", "pending"}
# keep categories flexible; we’ll normalize to lowercase and allow anything non-empty


def _read_csv(path: Path) -> pd.DataFrame:
    # read as strings first; we’ll coerce types carefully
    return pd.read_csv(path, dtype=str, skipinitialspace=True)


def validate_2022(df: pd.DataFrame) -> list[str]:
    issues: list[str] = []
    missing_cols = [c for c in EXPECTED_2022 if c not in df.columns]
    extra_cols = [c for c in df.columns if c not in EXPECTED_2022]
    if missing_cols:
        issues.append(f"2022 missing columns: {missing_cols}")
    if extra_cols:
        issues.append(f"2022 unexpected columns: {extra_cols}")

    # date parse check
    if "date" in df.columns:
        parsed = pd.to_datetime(df["date"], errors="coerce")
        bad = parsed.isna().sum()
        if bad:
            issues.append(f"2022 has {bad} unparsable date values")

    # status check (case-insensitive)
    if "status" in df.columns:
        st = df["status"].astype(str).str.strip().str.lower()
        bad_vals = sorted(set(st.dropna()) - ALLOWED_STATUS)
        if bad_vals:
            issues.append(f"2022 has unexpected status values: {bad_vals}")

    # value numeric check (allow missing)
    if "value" in df.columns:
        v = pd.to_numeric(df["value"], errors="coerce")
        # if value is non-empty but not numeric, it becomes NaN after coercion
        non_empty = df["value"].astype(str).str.strip().ne("") & df["value"].notna()
        bad = (v.isna() & non_empty).sum()
        if bad:
            issues.append(f"2022 has {bad} non-numeric 'value' entries")

    return issues


def validate_2023(df: pd.DataFrame) -> list[str]:
    issues: list[str] = []
    missing_cols = [c for c in EXPECTED_2023 if c not in df.columns]
    extra_cols = [c for c in df.columns if c not in EXPECTED_2023]
    if missing_cols:
        issues.append(f"2023 missing columns: {missing_cols}")
    if extra_cols:
        issues.append(f"2023 unexpected columns: {extra_cols}")

    if "date" in df.columns:
        parsed = pd.to_datetime(df["date"], errors="coerce")
        bad = parsed.isna().sum()
        if bad:
            issues.append(f"2023 has {bad} unparsable date values")

    if "status" in df.columns:
        st = df["status"].astype(str).str.strip().str.lower()
        bad_vals = sorted(set(st.dropna()) - ALLOWED_STATUS)
        if bad_vals:
            issues.append(f"2023 has unexpected status values: {bad_vals}")

    if "value" in df.columns:
        v = pd.to_numeric(df["value"], errors="coerce")
        non_empty = df["value"].astype(str).str.strip().ne("") & df["value"].notna()
        bad = (v.isna() & non_empty).sum()
        if bad:
            issues.append(f"2023 has {bad} non-numeric 'value' entries")

    return issues


def main() -> int:
    raw_dir = Path("data/raw")
    f2022 = raw_dir / "records_2022.csv"
    f2023 = raw_dir / "records_2023.csv"

    # If your instructor files have different names, rename them to these
    # or adjust Makefile inputs accordingly.
    if not f2022.exists() or not f2023.exists():
        print("ERROR: Expected raw files not found:")
        print(f" - {f2022} exists? {f2022.exists()}")
        print(f" - {f2023} exists? {f2023.exists()}")
        return 2

    df22 = _read_csv(f2022)
    df23 = _read_csv(f2023)

    issues = []
    issues.extend(validate_2022(df22))
    issues.extend(validate_2023(df23))

    if issues:
        print("VALIDATION FAILED:")
        for i in issues:
            print(f"- {i}")
        return 1

    print("VALIDATION OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
