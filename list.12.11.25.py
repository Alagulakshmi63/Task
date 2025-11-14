print("all prime numbers between 1 and 100 using a for loop at the end, print total count of prime number")
count=0
num=0
for num in range(2,101):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
         print(num, end="")
         count += 1
print("prime number count:",count)


print("pyramid pattern using nested for loops")
row=5
for i in range(1, row + 1):
    for j in range(row - i):
        print(" ",end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


print("calculate electricity bill if total bill is above 1000 add 10%surcharge")
unit=int(input("enter unit consumed: "))
if unit <= 100:
    bill=unit*1.5
elif unit<=200:
    bill=(100*1.5)+(unit-100)*2.5
elif unit<=300:
    bill=(100*1.5)+(100*2.5)+(unit-200)*4.0
else:
    bill=(100*1.5)+(100*2.5)+(100*4.0)+(unit-300)*5.0
if bill > 1000:
    bill+=bill*0.10
print(f"total bill: {bill:.2f}")
