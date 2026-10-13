"""
Student Performance Analysis & Merit List
BCA – Python Libraries and Applications | Lab Sheet 2

Run:
    pip install -r requirements.txt
    python student_analysis.py

The script answers Q1–Q33 from the lab sheet and exports student_merit_list.xlsx.
"""

import pandas as pd

data = {
    "RollNo": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Amit", "Neha", "Rahul", "Priya", "Rohan", "Kavya", "Arjun", "Simran"],
    "Department": ["BCA", "BCA", "MCA", "BCA", "MCA", "MCA", "BCA", "MCA"],
    "Age": [20, 21, 22, 20, 23, 22, 21, 24],
    "Marks": [85, 92, 67, 78, 88, 95, 55, 73],
}

df = pd.DataFrame(data)

def show(title, result):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")
    print(result)

# Level 1 — Basic
show("Q1. Complete DataFrame", df)
show("Q2. First 3 records", df.head(3))
show("Q3. Last 2 records", df.tail(2))
show("Q4. Number of rows and columns", df.shape)
show("Q5. Column names", df.columns.tolist())
show("Q6. Data types of all columns", df.dtypes)
show("Q7. Name column", df["Name"])
show("Q8. Name and Marks", df[["Name", "Marks"]])

# Level 2 — Selection and Filtering
show("Q9. Students who scored more than 80", df[df["Marks"] > 80])
show("Q10. Students who scored less than 70", df[df["Marks"] < 70])
show("Q11. Students with marks between 70 and 90 (inclusive)", df[df["Marks"].between(70, 90)])
show("Q12. BCA students", df[df["Department"] == "BCA"])
show("Q13. MCA students who scored more than 80", df[(df["Department"] == "MCA") & (df["Marks"] > 80)])
show("Q14. Students whose age is greater than 21", df[df["Age"] > 21])

# Level 3 — Data Analysis
show("Q15. Average marks", df["Marks"].mean())
show("Q16. Maximum marks", df["Marks"].max())
show("Q17. Minimum marks", df["Marks"].min())
show("Q18. Median marks", df["Marks"].median())
show("Q19. Number of students scoring above 75", (df["Marks"] > 75).sum())
show("Q20. Average marks of BCA students", df.loc[df["Department"] == "BCA", "Marks"].mean())
show("Q21. Average marks of MCA students", df.loc[df["Department"] == "MCA", "Marks"].mean())
show("Q22. Highest-scoring student", df.loc[[df["Marks"].idxmax()]])

# Level 4 — Data Manipulation
df["Bonus"] = 5
df["FinalMarks"] = df["Marks"] + df["Bonus"]
df["Result"] = df["Marks"].apply(lambda marks: "Pass" if marks >= 40 else "Fail")

def grade(marks):
    if marks >= 90:
        return "A+"
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B"
    if marks >= 60:
        return "C"
    return "D"

df["Grade"] = df["Marks"].apply(grade)
show("Q23–Q26. DataFrame with Bonus, FinalMarks, Result and Grade", df)

# Level 5 — Ranking
show("Q27. Students sorted by marks (high to low)", df.sort_values("Marks", ascending=False))
show("Q28. Top 3 students", df.nlargest(3, "Marks"))
df["Rank"] = df["Marks"].rank(ascending=False, method="min").astype(int)
show("Q29. DataFrame with Rank", df)

# Level 6 — Group Analysis
show("Q30. Number of students in each department", df.groupby("Department").size())
show("Q31. Average marks by department", df.groupby("Department")["Marks"].mean())
show("Q32. Maximum marks by department", df.groupby("Department")["Marks"].max())
show("Q33. Minimum marks by department", df.groupby("Department")["Marks"].min())
show("Department summary (count, mean, max, min)", df.groupby("Department")["Marks"].agg(["count", "mean", "max", "min"]))

# Challenge — final merit list, sorted highest to lowest
merit_list = df.sort_values("Marks", ascending=False)[
    ["Rank", "RollNo", "Name", "Department", "Marks", "Grade", "Result"]
].reset_index(drop=True)

output_file = "student_merit_list.xlsx"
merit_list.to_excel(output_file, index=False)
show("Challenge: Final student merit list", merit_list)
print(f"\nExcel merit list exported successfully to: {output_file}")
