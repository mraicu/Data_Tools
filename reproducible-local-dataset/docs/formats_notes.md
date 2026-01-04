# File Formats and Schema Evolution Notes

The raw datasets are kept in their original CSV format and are never modified to preserve
data integrity and traceability. Cleaned and harmonized outputs are stored both as CSV and
JSON to support different downstream use cases.

CSV is retained for compatibility with spreadsheets and simple command-line tools, while
JSON provides a structured, machine-readable format suitable for APIs and programmatic
consumption. During processing, the 2022 and 2023 schemas are harmonized by renaming
`source` to `source_system` and adding missing fields to older records. No semantic meaning
of the data is changed during format conversion.
