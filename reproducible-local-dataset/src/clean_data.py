from __future__ import annotations

from pathlib import Path

import pandas as pd


def normalize_common(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    # strip whitespace in all string fields
    for col in out.columns:
        out[col] = out[col].astype(str).str.strip()

    # normalize casing
    if "category" in out.columns:
        out["category"] = out["category"].str.lower()
    if "status" in out.columns:
        out["status"] = out["status"].str.lower()

    # parse date
    out["date"] = pd.to_datetime(out["date"], errors="coerce").dt.date

    # numeric value
    out["value"] = pd.to_numeric(out["value"].replace({"": None, "nan": None}), errors="coerce")

    return out


def clean_2022(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str, skipinitialspace=True)
    df = normalize_common(df)
    # rename to common name
    df = df.rename(columns={"source": "source_system"})
    # add 2023-only cols
    for c in ["department", "priority"]:
        df[c] = pd.NA
    df["year"] = 2022
    return df


def clean_2023(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str, skipinitialspace=True)
    df = normalize_common(df)
    # normalize source_system casing
    df["source_system"] = df["source_system"].str.lower()
    df["year"] = 2023
    return df


def main() -> int:
    raw_dir = Path("data/raw")
    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)

    f2022 = raw_dir / "records_2022.csv"
    f2023 = raw_dir / "records_2023.csv"

    df22 = clean_2022(f2022)
    df23 = clean_2023(f2023)

    # consistent column order
    cols = [
        "record_id",
        "date",
        "category",
        "value",
        "unit",
        "source_system",
        "status",
        "department",
        "priority",
        "year",
    ]
    df22 = df22[cols]
    df23 = df23[cols]

    df_all = pd.concat([df22, df23], ignore_index=True)

    df22.to_csv(out_dir / "records_2022_clean.csv", index=False)
    df23.to_csv(out_dir / "records_2023_clean.csv", index=False)
    df_all.to_csv(out_dir / "records_all_clean.csv", index=False)

    print("CLEAN OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
