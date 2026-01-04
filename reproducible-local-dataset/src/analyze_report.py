from __future__ import annotations

from pathlib import Path

import pandas as pd


def main() -> int:
    in_path = Path("data/processed/records_all_clean.csv")
    reports_dir = Path("reports")
    reports_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(in_path)

    # Basic summaries
    n_rows = len(df)
    n_missing_value = df["value"].isna().sum()

    by_year = df.groupby("year").size().rename("n_records").reset_index()
    by_category = df.groupby(["year", "category"]).size().rename("n_records").reset_index()
    by_status = df.groupby(["year", "status"]).size().rename("n_records").reset_index()

    by_year.to_csv(reports_dir / "records_by_year.csv", index=False)
    by_category.to_csv(reports_dir / "records_by_year_category.csv", index=False)
    by_status.to_csv(reports_dir / "records_by_year_status.csv", index=False)

    # short markdown report
    md = []
    md.append("# Records Dataset Report")
    md.append("")
    md.append(f"- Total cleaned records: **{n_rows}**")
    md.append(f"- Missing numeric values (`value`): **{n_missing_value}**")
    md.append("")
    md.append("## Outputs")
    md.append("- `reports/records_by_year.csv`")
    md.append("- `reports/records_by_year_category.csv`")
    md.append("- `reports/records_by_year_status.csv`")
    md.append("")
    md.append("## Notes")
    md.append("- 2022 and 2023 were harmonized into a shared schema (`source` → `source_system`).")
    md.append("- `department` and `priority` are only present in 2023; they are blank for 2022.")
    md.append("")

    (reports_dir / "report.md").write_text("\n".join(md), encoding="utf-8")

    print("REPORT OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
