print("create a tuple")
a=(1,2,3,4,5,6,7,8,9)
print(tuple(a))


print("find th size of a tuple")
a=(1,2,3,4,5,6,7,8,9)
a1=len(a)
print("tuple:",a)
print("size of a tuple:",a1)


print("sort tuples")
b=[23,53,73,84,3,55,25,36]
b2=sorted(b)
print("sorted:",b2)

print("create a tuple with different data types")
c=("alagu",23,5.12,True)
for d in c:
    print(d)
    print(type(d))


print("unpack a tuple in several variables")
e=("apple","orange","banana","dragan furit","grapes")
(a,b,c,d,f)=e
print("C value is:",c)


print("convert a tuple to a string")
f=("a","l","a","g","u")
g=''.join(f)
print(type(f))
print("convert after string value:",g)


print("4th element and 4 th element last")
h=(34,55,66,77,88,99,33,22,11)
forth_element=h[4]
forth_element_last=h[-4]
print("forth_element is:",forth_element)
print("forth_element_last:",forth_element_last)


print("find th repeated items of a tuple")
j=(22,42,35,56,78,22,23,22,25,35,22)
repeated_value=[k for k in set(j) if j.count(k) > 1]
print("repeated_value is:",repeated_value)


print("To Check whether an element exists or not")
t2=(34,56,23,25,81)
x=int(input("Enter element to check: "))
if x in t2:
    print(x,"exists in the tuple")
else:
    print(x,"doesn't exist in the tuple")
print()


print("Convert a list to a tuple")
lis=[1,2,3,4]
print(lis)
print(tuple(lis))
print()


print("Remove an item from a tuple")
tup2=(1,2,3,4,5)
li5=list(tup2)
li5.remove(3)
tup2=tuple(li5)
print("Tuple after Removing 4th element: ",tup2)
print()


print("Slicing a tuple")
print(tup2)
print("First Two Elements: ",tup2[:2])
print("Last Two Elements: ",tup2[-2:])
print()


print("Finding the index of an item in a tuple")
tup3=(5,10,15,20,25)
print("Index of 15 is: ",tup3.index(15))
print()


print("Finding the Length of Tuple")
print(tup3)
print(len(tup3))
print()


print("Reversing a Tuple")
print(tup2)
print("Reversed Tuple: ",tup[::-1])
print()


print("Converting a given string list to a tuple")
list2=['Almond','Cake','Berries','Dragon Fruit']
print(tuple(list2))
