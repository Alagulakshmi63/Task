import pandas as pd

data = {"Name": ["Ravi", "Ravi", "Anu", "Anu", "Kiran", "Kiran"],"Department": ["IT", "IT", "HR", "HR", "IT", "HR"],"Month": ["Jan", "Feb", "Jan", "Feb", "Jan", "Feb"],"Salary": [30000, 32000, 28000, 29000, 35000, 36000]}
df = pd.DataFrame(data)
print(df)


"Q1. Find total and maximum salary for each employee"
q1=df.groupby("Name")["Salary"].agg(["sum","max"])
print(q1)


"Q2. Find average salary for each department and sort it descending"
q2=df.groupby("Department")["Salary"].mean().sort_values(ascending=False)
print(q2)

"Q3. Find department-wise total salary for only February"
q3=df[df["Month"]=="Feb"].groupby("Department")["Salary"].sum()
print(q3)

"Q4. Find employees whose total salary is greater than 60,000"
q4=df.groupby("Name")["Salary"].sum()
q4=q4[q4 > 60000]
print(q4)


"Q5. Find month-wise total salary for each department"
q5=df.groupby(["Department","Month"])["Salary"].sum()
print(q5)


"Q6. Find department-wise salary count, sum, and average"
q6=df.groupby("Department")["Salary"].agg(["count","sum","mean"])
print(q6)


"Q7. Find which month has the highest total salary"
q7 = df.groupby("Month")["Salary"].sum().idxmax()
print(q7)


"Q8. Add a column showing department average salary using transform()"
df["Dept_Avg_Salary"] = df.groupby("Department")["Salary"].transform("mean")
print(df)

"Q9. Find employees whose salary is above their department’s average"
df["Dept_Avg"] = df.groupby("Department")["Salary"].transform("mean")
q9 = df[df["Salary"] > df["Dept_Avg"]]
print(q9)


"Q10. Convert department-wise total salary into a dictionary"
q10 = df.groupby("Department")["Salary"].sum().to_dict()
print(q10)


