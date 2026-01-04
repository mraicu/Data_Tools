# Command-Line Dataset Exploration (CLI Notes)

This section documents common command-line operations used to explore and inspect the
dataset without opening it in a spreadsheet or script. Examples are provided for both
**Windows PowerShell** and **Unix-like shells**.

---

## 1. Count total number of records in a CSV file

**PowerShell**

```powershell
(Get-Content data/raw/records_2022.csv | Measure-Object -Line).Lines - 1
```

**Unix**

```powershell
wc -l data/raw/records_2022.csv
```

Explanation:
Counts the number of rows in the dataset. The header row is excluded to obtain the true
number of records.

## 2. Search for cancelled records

```powershell
Select-String "cancelled" data/raw/records_2022.csv
```

**Unix**

```powershell
grep "cancelled" data/raw/records_2022.csv
```

Explanation:
Searches the dataset for records marked as cancelled, useful for auditing data quality
or filtering invalid entries.

## 3. Extract a single column (status)

**PowerShell**

```powershell
Import-Csv data/raw/records_2022.csv | Select-Object -ExpandProperty status
```

**Unix**

```powershell
cut -d, -f7 data/raw/records_2022.csv
```

## 4. Count records by category

**PowerShell**

```powershell
Import-Csv data/raw/records_2022.csv |
  Group-Object category |
  Select-Object Name, Count
```

**Unix**

```powershell
cut -d, -f3 data/raw/records_2022.csv | sort | uniq -c

```

Explanation:
Groups records by category and counts how many times each category appears.

## 5. Redirect filtered output to a file

**PowerShell**

```powershell
Select-String "medication" data/raw/records_2023.csv |
  Out-File docs/medication_records_2023.txt

```

**Unix**

```powershell
grep "medication" data/raw/records_2023.csv > docs/medication_records_2023.txt
```

Explanation:
Filters records related to medication and saves the result to a file for later inspection
or reporting.
