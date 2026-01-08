import pandas as pd


"DataFrame Creating"
data={"Name":["John","Sara","Mike",None,"Anna"],"Age":[25,30,None,22,28],"City":["New York",None,"London","Paris",None]}
df=pd.DataFrame(data)
print("Before Cleaning:",df)


"Remove all rows where city columns missing"
df=df.dropna(subset=["City"])



"Fill missing age values with the avg"
avg_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(avg_age)



"Replace missing Name with Unknown"
df["Name"] = df["Name"].fillna("Unknown")
print("After Cleaning:")
print(df)


"Topic 1: Handling Missing Values"
import pandas as pd

"Task 1: Create a DataFrame with missing values"
data={"Name":["John","Sara","Mike",None,"Anna"],"Age":[25,30,None,22,28],"City":["Chennai","Madurai","London","Bangalore",None],"Salary":[40000, 50000, 45000, 38000, 42000]}
df = pd.DataFrame(data)
print(df)


"Task 2: Check total missing values in each column"
print(df.isnull().sum())

"Task 3: Remove rows where City is missing"
df = df.dropna(subset=["City"])
print("After removing rows where City is missing:",df)


"Task 4: Fill missing Age values with column average"
avg_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(avg_age)

print("After filling missing Age with average:",df)


"Task 5: Replace missing Name values with Unknown"
df["Name"] = df["Name"].fillna("Unknown")
print(df)


"Topic 2: DataFrame Attributes"
"Task 6: Print the shape of the DataFrame"
print(df.shape)

"Task 7:Display all column names"
print(df.columns)

"Task 8:Check the data types of each column"
print(df.dtypes)


"Task 9:Set Name as the index"
df.set_index("Name",inplace=True)
print(df)

"Task 10:Reset the index back to default"
df.reset_index(inplace=True)
print(df)


"Topic 3: Sorting &amp; Updating Data"
"Task:11 Sort the DataFrame by Age in ascending order"
df_sorted_age = df.sort_values(by="Age", ascending=True)
print(df_sorted_age)


"Task:12 Sort the DataFrame by Salary in descending order"
df_sorted_Salary = df.sort_values(by="Salary", ascending=False)
print(df_sorted_Salary)

"Task:13 Increase Salary by 5000 for employees whose Age>30"
df.loc[df["Age"] >= 30, "Salary"] = df["Salary"] + 5000
print(df)

"Task:14 Replace Chennai with Chennai City in the City column"
df["City"] = df["City"].replace("Chennai", "Chennai City")
print(df)

"Task 15: Add New Row"
df.loc[5] = ["David", 35, "Mumbai", 60000]
print(df)


"Topic 4: Conditional Selection &amp; Boolean Logic"
"Task 16: Display employees whose Salary is greater than 40000"
print(df[df["Salary"] > 40000])


"Task 17: Show only Name and Salary for employees in Bangalore"
print(df[df["City"] == "Bangalore"][["Name", "Salary"]])

"Task 18: Create a new column Status where Salary>40000"
df["Status"] = df["Salary"] > 40000
print(df)

"Task 19:Count how many employees belong to each City"
print(df["City"].value_counts())

"Task 20:Select employees whose Age is between 25 and 35"
print(df[df["Age"].between(25, 35)])


"Topic 5: Import, Export &amp; Viewing Data"
"Task 21:Export the DataFrame to a CSV file"
df.to_csv("employees.csv", index=False)

"Task 22:Import the CSV file back into Pandas"
df_new = pd.read_csv("employees.csv")
print(df_new)

"Task 23: Display the first 5 rows using head()"
print(df_new.head(4))

"Task 24:Display the last 3 rows using tail()"
print(df_new.tail(3))


"Task 25:Check if the DataFrame contains any missing values"
print(df_new.isnull().any())


