# Data Dictionary

This document describes the variables present in the 2022 and 2023 records datasets.

## Common Columns (Both Years)

| Column Name | Type   | Description              | Units      | Allowed Values                            | Missing Meaning               |
| ----------- | ------ | ------------------------ | ---------- | ----------------------------------------- | ----------------------------- |
| record_id   | string | Unique record identifier | N/A        | Alphanumeric                              | Not allowed                   |
| date        | date   | Date of record event     | YYYY-MM-DD | Valid dates                               | Unknown date                  |
| category    | string | Record category          | N/A        | admission, discharge, medication, imaging | Unknown category              |
| value       | float  | Recorded numeric value   | See unit   | ≥ 0                                       | Not recorded / not applicable |
| unit        | string | Measurement unit         | varies     | ml, count, points, dose                   | Unknown unit                  |
| status      | string | Record status            | N/A        | ok, cancelled, pending                    | Unknown status                |

## 2022-Only Columns

| Column Name | Type   | Description                             |
| ----------- | ------ | --------------------------------------- |
| source      | string | Originating system or data entry source |

## 2023-Only Columns

| Column Name   | Type   | Description            | Allowed Values         |
| ------------- | ------ | ---------------------- | ---------------------- |
| source_system | string | Originating system     | SYSTEM_A, manual_entry |
| department    | string | Responsible department | RAD, WARD_B, etc.      |
| priority      | string | Processing priority    | low, medium, high      |

## Notes on Schema Evolution

-   Column `source` (2022) was renamed to `source_system` in 2023.
-   Additional operational fields (`department`, `priority`) were introduced in 2023.
-   Cleaning scripts harmonize column names and value casing across years.
