print("right triangle")
for i in range(1,12):
    for j in range(1,i+1):
        print("*",end="")
    print()


print("left triangle")
for i in range(6):
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print()


print("square")
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()


print("8")
for i in range(7):
    for j in range(5):
        if(i in [0, 3, 6]) and (j > 0 and j < 4):
            print("*",end="")
        elif(j in [0, 4]) and (i not in [0, 3, 6]):
            print("*",end="")
        else:
            print(" ",end="")
    print()


print("hollow square pattern")
for i in range(10):
    for j in range(10):
        if i == 0 or i == 10-1 or j == 0 or j == 10-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("hollow right triangle")
for i in range(1,7 + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 7:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("inverse left striangle")
for i in range(8, 0,-1):
    for j in range(i):
        print("*",end="")
    print()


print("inverse right triangle")
for i in range(9, 0, -1):
    for j in range(9 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()


print("pattern 1")
rows=5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("pattern 2")
rows=5
for i in range(rows, 0,-1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()



print("pattern 3")
row=5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("", end="")
        if j == 1 or j == i or i == rows:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()


print("pattern 4")
rows=6
for i in range(rows):
    ch = chr(65 + i)
    print(ch * (i + 1))


print("pattern 5")
rows=5
ch=65
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(ch), end="")
        ch += 1
    print()


print("pattern 6")
rows=5
for i in range(rows):
    ch = chr(65 + i)
    print(ch * (i + 1))


print("pattern 7")
rows=5
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end="")
    print()
    

    
