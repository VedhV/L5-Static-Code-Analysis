# Lab 5: Static Code Analysis

## Objective
Analyze and improve a Python auction-bidding program using Pylint, Bandit, and Flake8.

## Tools Used
- **Pylint:** Code quality and maintainability.
- **Bandit:** Security vulnerability detection.
- **Flake8:** Code style and formatting.

## Issues Fixed
- Removed unsafe XML-RPC integration.
- Escaped untrusted text before rendering HTML.
- Enforced reserve prices and minimum bid increments.
- Prevented sellers from bidding on their own auctions.
- Corrected auction closing-time validation.
- Improved documentation, naming, and formatting.

## Final Results
- **Pylint:** 10.00/10
- **Bandit:** No issues identified.
- **Flake8:** No violations reported.

## Files
- `auction_system.py` — Cleaned Python program.
- `issues.md` — Issues identified and fixes applied.
- `reflection.md` — Lab reflection answers.
- `lab5_output/` — Supporting code and analysis reports.
- `pylint_after.txt`, `bandit_after.txt`, `flake8_after.txt` — Final analysis reports.

## Run the Program
```bash
python auction_system.py
```
