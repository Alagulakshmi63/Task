import pandas as pd
"Series Create"
A=[5,10,15,20]
S=pd.Series(A)
print(S)


"Custom index"
A=[5,10,15,20]
S=pd.Series(A,index=['W','X','Y','Z'])
print(S)


"Create Data Frame"
B={"Name":["Ravi","Kiran","Meena"],"Age":[22,25,28],"City":["Chennai","Bangalore","Hyderabad"]}
C=pd.DataFrame(B)
print(C)

"Create Operation_Single_Columns"
print(C["Name"])


"Create Operation_Multi_Columns"
print(C[["Name","City"]])


"Data frame Row Operations_loc"
print(C.loc[1])


"Data frame Row Operations_iloc"
print(C.iloc[1])


"Data Frame Slicing_first two"
print(C[0:2])

"Data Frame Slicing_age>23"
print(C[C["Age"]>23])


"Add New Column"
C["Salary"]=[30000,40000,50000]
print(C)


"Modify a Column"
C["Age"]=C["Age"]+1
print(C)


"Conditional Update"
C.loc[C["Name"]=="Kiran","Age"]+=1
print(C)


