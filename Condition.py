print("Write a Python program to check whether a number is positive, negative, or zero.")
number=int(input("enter your number"))
if(number>0):
    print("positive")
elif(number<0):
    print("negative")
elif(number==0):
    print("zero")
print("Write a program to check whether a number is even or odd.")
if(number%2==0):
    print("even")
elif(number%2==1):
    print("odd")
print("Write a program to check if a person is eligible to vote (age ≥ 18).")
age=12
if(age>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
print(" Write a program to check if a student passed or failed based on marks.")
sub1=86
sub2=78
sub3=66
sub4=88
sub5=67
if(sub1>=40 and sub2>=40 and sub3>=40 and sub4>=40 and sub5>=40):
    print("pass")
else:
    print("fail")
print("Write a program to find the largest of two numbers.")
num1=33
num2=40
if num1 > num2:
    print(f"the largest num is: {num1}")
elif num2 > num1:
    print(f"the largest num is: {num2}")
else:
    print("both numbers are equal")
print("Write a program to display grade (A, B, C, D, Fail) based on marks.")
marks=int(input("enter your marks"))
if marks>90 and marks <=100:
    print("A grade")
elif marks>80 and marks <=90:
    print("B grade")
elif marks>70 and marks <=80:
    print("C grade")
else:
    print("D grade")
