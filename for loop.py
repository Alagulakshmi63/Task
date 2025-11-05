print("1 and that are divisible by 6 but not by 9")
for i in range(1,101):
    if i%6==0 and i%9!=0:
        print(i)
print("sum of all odd num from 1 to 50")
num=0
for i in range(1,51,2):
    num+=i
print(num)
print("sum of all even num from 1 to 50")
num=0
for i in range(1,51,1):
    num+=i
print(num)
print("count 1to 200 divisible by both 4 and 6")
count=0
for i in range(1,201):
    if i%4==0 and i%6==0:
        count+=1
print(count)
print("malytiplication table")
num=int(input("enter you number"))
for i in range(1,11):
    print(f"{num} x {i}={num*i}")


print("factorial")
sum=1
n=int(input("enter your number"))
for i in range(1,n+1):
    sum*=i
print(sum)

print("=======prime number between 1 and 50=========")
for num in range(2,51):
    count=0
    for i in range(2,num):
        count+=(num%i==0)
    if count==0:
                print(num)
print("arithmetic")
num=int(input("enter your number:"))
n=num
sum=0
num_digit=len(str(num))
for i in range(num_digit):
    digit=n%10
    sum+=digit
    n=n//10
    print(i)
print("sum:",sum)
print("how many numbers between 1 and 500 are perfect cubes")
count=0
for i in range(1,501):
    cube=round(i**(1/3))
    if cube **3==i:
        count+=1
        print(i)
print("count 1,500:",count)
print("reverse number in arithmetic")
num=int(input("enter your nume"))
n=num
reverse_num=0
for i in range(count):
        digit=n%10
        reverse_num=reverse_num*10+digit
        n//=10
print("reverse num:",reverse_num)
print(" 1 to 100 but skip numbers ending with digit 5")
for i in range(1,101):
    if i%10==5:
        print(i)



