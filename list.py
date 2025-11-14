print("reverse a given list in python")
L=[100,200,300,400,500]
a=L[::-1]
print(a)

print("Concateate two lists")
list1=["Hello", "Madam"]
list2=["Dear", "Sir"]
b=list1+list2
print(b)


print("remove empty string from the list of strings")
list1=["Pen","","Pencil","Eraser","","Scale"]
list1.remove("")
list1.remove("")
print(list1)

list1=["Pen","","Pencil","Eraser","","Scale"]
f=[s for s in list1 if s !=""]
print(f)


print("write a python program to convert a string to a list")
a="apple"
b=list(a)
print(b)


print("check if a list contains an element")
c=[1,2,3,'a','b','c']
if 3 in c:
    print("3 in list")
else:
    print("3 not in list")


print("remove all elements from a list")
a=[23,54,22,32,44]
a.clear()
print(a)


print("count the occurrence of a specific object in a list")
pets=['dog','cat','fish','fish','cat']
c=input("enter the pet to count:")
count=pets.count(c)
print(f"the pet '{c}' appears {count}times in the list")


print("return the length of a list")
a=input("enter list elements separated by spaces:")
a.split()
length=len(a)
print("lenth of the list:",length)


print("insert a value at a specific index in an exiting list")
d=[10,20,30,40,50,60]
value=input("enter the value to insert:")
index=int(input("enter the index position:"))
d.insert(index, value)
print("after list:",d)


print("write a python program to clone or copy a list")
f=["alagu","lakshmi","m"]
e=f.copy()
print(e)


