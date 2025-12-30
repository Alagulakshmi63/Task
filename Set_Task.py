"create_set"
students={"Ravi","Anu","Karthi","Anu","Meena"}
print("Create Set:",students)


"Add_Elements"
students={"Ravi","Anu","Karthi","Anu","Meena"}
students.add("Suresh")
print("Add Elements:",students)



"Update_set"
students={"Ravi","Anu","Karthi","Anu","Meena"}
new_student={"Divya","Ravi"}
students.update(new_student)
print("Update:",students)


"Remove_Elements"
students={"Ravi","Anu","Karthi","Anu","Meena"}
students.remove("Meena")
print("Remove:",students)
students.discard("Arun")
print("Discard:",students)



"Pop and Clear"
students={"Ravi","Anu","Karthi","Anu","Meena"}
students.pop()
print("Pop:",students)
students.clear()
print("Clear:",students)



"Join_Sets"
"Create Two set"
A={10,20,30,40}
B={30,40,50,60}

"Find Union"
a={10,20,30,40}
b={30,40,50,60}
print("Union:",a.union(b))
print("Intersection:",a.intersection(b))
print("Difference(a-b):",a.difference(b))
print("Symmetric_Difference:",a.symmetric_difference(b))

