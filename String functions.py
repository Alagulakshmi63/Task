print("string to end of another strin")
a="Welcome"
b="Tenkasi"
c=a+b
print(c)

print("specified sequence of char value")
D="Alagulakshmi"
E="mi"
if(E in D):
    print("yes")
else:
    print("no")

print("character in strin to lowercase")
f="LAKSHMI"
g=f.lower()
print(g)

print("leadting or tailing whitespace from string")
h="   Alagu   "
i=h.strip()
print(i)

print("reverse a string")
j="Alagu"
k=j[::-1]
print(k)

print("replace all spaces with underscores")
l="hi everyone"
m=l.replace(" ","_")
print(m)

print("middle three characters")
o="python123"
mid=len(o)//2
p=o[mid-1:mid+2]
print(p)

print("first and last latter to capital")
q="alagu"
for i in q:
    if not i.isdigit():
        q=q[0].upper()+q[1:+1]+q[-1].upper()
print(q)

print("length of a given string")
name=input("enter your name:")
length=len(name)
print("length of a name:",length)

print("no of occurrence of a given string with repetition")
r="i am new to this office but not new to remove digits in strings"
word="new"
count=r.count(word)
print("the word",word,"apper",count,"times in string")

print("replace a specified character with another character")
text="the quick brown fox jumps over the lazy dog"
old="fox"
new="***"
now=text.replace(old,new)
print(now)

print("count vowels in a string")
word="I Love India"
vowels="aeiouAEIOU"
count=0
for char in word:
    if char in vowels:
        count+=1
print("number of vowels:",count)


print("string contains only whitespace")
text="welcome_all"
if text.strip()=="":
    print("only whitespace")
else:
    print("string contain non-whitespace")

print("remove all digits from string")
t="alagulakshmi6369gmail"
run=''.join([ch for ch in t if not ch.isdigit()])
print(run)

print("find the lenth of your name using len()")
m1="arulkumar"
print("name",len(m1))


print("string to uppercase using upper()")
name="mariyappan"
i=name.upper()
print(i)

print("string to lowercase using lower")
name="mariyappan"
u=name.lower()
print(u)

print("a in appears in a string using count()")
na="appears"
word="a"
count=na.count(word)
print("the word",word,"apper",count,"times in string")


print("starting stars wuth the word hello using starswith()")
nam="hello world"
if nam.startswith("hello"):
    print("yes,string startswith hello")
else:
    print("no,string starswith hello")

print("end with .com using endswith()")
name="alagulakshmi6369@gmail.com"
if name.endswith(".com"):
    print("correct")
else:
    print("not correct")


print("python in a sentence using find()")
sentence="I am leaning python programming"
position=sentence.find("python")
if position !=-1:
    print(f"python found")
else:
    print("python not found")

print("java with python in a sentence using replace()")
n2="i am leaning java programming"
n3=n2.replace("java","python")
print(n3)

print("remove extra space from both sides of string using strip()")
names="     Alagu lakshmi     "
x=names.strip()
print(x)

print("capitalize the first letter of a sentence using capitalize()")
names="alagu lakshmi"
y=names.capitalize()
print(y)


print("split a sentence into words using split()")
senten="i love india"
z=senten.split()
print(z)

print("join a list of wors using join()")
senten="i am going to chennai", "2026"
z2=("".join(senten))
print(z2)


print("string has only alphabets using isalpha()")
c2="alagu6369"
print("alphabets",c2.isalpha())


print("string has only numbers using isdigit()")
a4="1234567"
print("number",a4.isdigit())


print("string has both letters and numbers using isalnum()")
s3="alagulakshmi12052002"
s4="alagu@6369"
print(s3.isalnum())
print(s4.isalnum())


print("string are in lowercase using islower()")
d2="Mariyappan"
print(d2.islower())


print("string are in uppercase using isupper()")
f4="ALAGULAKSHMI"
print(f4.isupper())

print("swap lowercase to uppercase and vice versa using swapcase()")
g2="AlAgU LaKsHmI"
print(g2.swapcase())


print("convert every word first letter to uppercase using title()")
h2="i have one pen"
print(h2.title())


print("string contains only spaces using isspace()model 1")
text="    "
print(text.isspace())

print("string contains only spaces using isspace() model 2")
text="Hello all"
if text.isspace():
    print("string contain only space")
else:
    print("string contain non-space")


print("count the number of vowels in a given string")
word="kamarajar government arts and science collage"
vowels="aeiouAEIOU"
count=0
for char in word:
    if char in vowels:
        count+=1
print("number of vowels:",count)


print("check if a given word is a pslindrome")
word="ramar"
if word==word[::-1]:
    print("the word is a palindrome")
else:
    print("the word is not a palindrome")

print("remove all digits from given string")
text="i have 2 apple"
result=''.join([char for char in text if not char.isdigit()])
print("string remove all digits:",result)


print("replace all space in a sentence with undersoures")
w3="welcome to all in tenkasi"
w4=w3.replace(" ","_")
print(w4)


print("extract only numbers from a mixed string like abc123xyz")
j="alagu12052002lakshmi"
numbers=''.join([char for char in j if char.isdigit()])
print("numbers extract:",numbers)

print("print all word in a sentence start with a capital letter")
sen="python is fun and easy lean"
q3=sen.title()
print(q3)

print("how many times each letter occurs")
gf="I have one sentence"
sent=gf.lower()
letter_count={}
for char in sent:
    if char.isalpha():
        letter_count[char]=letter_count.get(char,0)+1
for letter,count in letter_count.items():
    print(f"{letter}:{count}")
    

print("remove all punctuation")
import string
nama="hi! how are you?"
result=''.join([char for char in nama if char not in string.punctuation])
print(result)


print("check end with @gamil.com")
my="alagulakshmi@gmail.com"
print(my.endswith("@gmail.com"))


print("reverse a string without using slicing")
text="welcome"
re=""
for char in text:
    re=char+re
print("reverse string:",re)
