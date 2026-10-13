# Student Performance Analysis & Merit List

**Mini-project title:** Student Performance Analysis and Merit List Generator using Python and Pandas

## Overview
This mini-project solves all 33 questions in the BCA *Python Libraries and Applications – Lab Sheet 2*. It demonstrates DataFrame creation, selection, filtering, descriptive statistics, calculated columns, grading, ranking, group analysis, and Excel export.

## Dataset
The sample dataset contains 8 students with these fields:
- RollNo
- Name
- Department
- Age
- Marks

## Requirements
- Python 3.9+
- pandas
- openpyxl

## Run on macOS / Windows
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python student_analysis.py
```
On Windows Command Prompt, activate with `.venv\Scripts\activate` and run `python student_analysis.py`.

The script prints the answers for Q1–Q33 and creates `student_merit_list.xlsx` in the current folder.

## Project structure
```text
Student_Performance_Analysis/
├── student_analysis.py
├── requirements.txt
└── README.md
```

## Concepts demonstrated
- Pandas DataFrame and column inspection
- Filtering with conditions
- Mean, median, min, max and counts
- Bonus and final marks calculation
- Pass/fail result and grade assignment
- Sorting and ranking
- `groupby()` aggregation
- Exporting a merit list to Excel

## Data note
This project uses the sample student data provided in the lab sheet. It is an educational demonstration, not a production student-record system.
