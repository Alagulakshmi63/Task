"Findkey using **kwargs"
def find_key(search_key,**data):
    if search_key in data:
        print("key found")
    else:
        print("key not found")
find_key("age",name="Alagu",age=23,city="Tenkasi")



"Findvalue using **kwargs"
def find_value(search_value,**data):
    if search_value in data.values():
        print("value Found")
    else:
        print("value not Found")
find_value("Alagu",name="Alagu",age=23,city="Tenkasi")


"Sum all numbers using **kwargs"
def total(*n):
    print(sum(n))
total(1,2,3,4,5,6,7)


"even num using **kwargs"
def even_num(*nums):
    for i in nums:
        if i%2==0:
            print(i)
even_num(1,2,3,4,5,6,7,8,9,10)

"Pertfect Num Check"
def perfect_number(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

perfect_number(6)


"Dictionary last key remove"
def remove_last_key(**Z):
    last_key = list(Z.keys())[-1]
    Z.pop(last_key)
    print(Z)

remove_last_key(a=10, b=20, c=30)


"Simple Calculator Functions"
def calculator(a, b, op):
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("Invalid Operator")

calculator(10, 5, "+")

"String Palindrome"
def palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

palindrome("madam")

"Vowels,Conssonants,Spl Characters"
def count_characters(s):
    vowels = consonants = special = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
        else:
            special += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Special Characters:", special)

count_characters("Hello@123")
