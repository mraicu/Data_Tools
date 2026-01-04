# Integrity Notes (Checksums)

This project uses SHA-256 checksums to detect accidental changes or corruption in the
raw input dataset located in `data/raw/`.

## Where the manifest is stored

-   `docs/checksums.sha256`

Each line contains:

-   SHA-256 hash
-   relative file path (e.g., `data/raw/records_2022.csv`)

## How to verify checksums (Windows PowerShell)

From the project root, run:

```powershell
Get-Content docs/checksums.sha256 | ForEach-Object {
  if ($_ -match '^([0-9a-f]{64})\s+(.+)$') {
    $expected = $matches[1]
    $path = $matches[2]
    $actual = (Get-FileHash $path -Algorithm SHA256).Hash.ToLower()
    if ($actual -eq $expected) {
      "OK  $path"
    } else {
      "FAIL  $path"
      "  expected: $expected"
      "  actual:   $actual"
    }
  }
}
```
