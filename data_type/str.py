
"""TO SORT ALPHANUMERIC
 OUTPUT-ABD134"""
s1 = 'B9Adabvxg5D13'
alpha = []
num = []
for i in s1:
    if i.isalpha():
        alpha.append(i)
    if i.isdigit():
        num.append(i)

print(alpha)
print(num)
sort = ' '.join(sorted(alpha) + sorted(num))
print("sorted alphanumeric in string", sort)

name = "Jamesh"
res = name[0]
l = len(name)
mid = int(l / 2)
res = res + name[mid]
res = res + name[-1]
print(res)

'''Count all letters, digits, and special symbols from a given string'''
str1 = "P@#yn26at^&i5ve"
ch = 0
di = 0
sp = 0
sum_digit = 0
for i in str1:
    if i.isalpha():
        ch += 1
    elif i.isdigit():
        di += 1
        sum_digit += int(i)
    else:
        sp += 1
print("char:", ch)
print("digit:", di)
print("special symbol:", sp)
print("sum of digit in string data:", sum_digit)

"""Arrange string characters such that lowercase letters should come first"""
str1 = 'PyNaTive'
lower = []
upper = []
for char in str1:
    if char >= 'a' and char <= 'z':
        lower.append(char)
    else:
        upper.append(char)
print(lower)
print(upper)
res = ''.join(lower + upper)
print(res)

"""Given two strings, s1 and s2.
 Write a program to create a new string s3 made of the first char of s1, 
 then the last char of s2, Next, the second char of s1 and second last char of s2, and so on.
  Any leftover chars go at the end of the result."""
s1 = "Abc"
s2 = "Xyz"
s = " "
s2 = s2[::-1]
i = j = 0
while i < len(s1) or j < len(s2):
    if i < len(s1):
        s = s + s1[i]
        i += 1
    if j < len(s2):
        s = s + s2[j]
        j += 1
print(s)

"""Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
The character’s position doesn’t matter."""


def check_balance(S1, S2):
    result = True
    for char in S1:
        if char in S2:
            continue
        else:
            result = False
    return result


s1 = "Yn"
s2 = "PYnative"
flag = check_balance(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = check_balance(s1, s2)
print("s1 and s2 are balanced:", flag)
print("*********************************")
str1 = "/*Jon is @developer & musician"
# replace special symbols with ''
res = re.sub('[^\w\s]', '', str1)
print("New string is ", res)

"""Given two strings, s1 and s2.
 Write a program to create a new string s3 by appending s2 in the middle of s1."""
s1 = "Ault"
s2 = "Kelly"
s = " "
mid = int(len(s1) / 2)
s = s + s1[:mid]
print(s)
s = s + s2
print(s)
s += s1[mid:]
print(s)

s1 = "America"
s2 = "Japan"
s = " "
mid = int(len(s1) / 2)
s += s1[:mid]
s += s2
s += s1[mid:]
print(s)

str1 = "Welcome to USA . usa awesome, isn't it?"
x = str1.split()
print(x)
count = 0
for char in x:
    if char.lower() == "usa":
        count += 1
print(count)

"""Write a program to count occurrences of all characters within a string"""
str1 = "akebaaaabk"
dict = {}
for char in str1:
    dict[char] = dict.get(char, 0) + 1
print(dict)
s = " "
for k, v in dict.items():
    s += k + str(v)
print(s)

"1.length of string"
data = "Hello World"
print("***********First way ***************")
print(len(data))
print("**************SECOND WAY **************")
counter = 0
for i in data:
    counter += 1
print(counter)

print("*********Third way**************")


# main program
def countdata(n):
    count = 0
    for i in n:
        count += 1
    print(count)


data = "Hello World"
countdata(data)

print("***************Four way***************")


class counter:
    def get_count(self):
        self.data = "Hello world"
        countval = 0
        for i in self.data:
            countval += 1
        print(countval)


ob = counter()
ob.get_count()

"2.count characters in string "
data = "sadsfdgfabaaaasd"
cs = 0
ca = 0
cf = 0
for char in data:
    if char == "s":
        cs += 1
    if char == "a":
        ca += 1
    if char == "f":
        cf += 1
print("count of s:{}".format(cs))
print("count of a:", ca)
print("count of f:", cf)

print("*********second way*****************")


def counter_char():
    data = "sadsfdgfabaaaasd"
    cs = 0
    ca = 0
    cf = 0
    for char in data:
        if char == "s":
            cs += 1
        if char == "a":
            ca += 1
        if char == "f":
            cf += 1
    print("count of s:{}".format(cs))
    print("count of a:", ca)
    print("count of f:", cf)


counter_char()
print("********* Third way *****************")


class count_char:
    def get_char(self):
        self.data = "sadsfdgfabaaaasd"
        cs = 0
        ca = 0
        cf = 0
        for char in self.data:
            if char == "s":
                cs += 1
            if char == "a":
                ca += 1
            if char == "f":
                cf += 1
        print("count of s:{}".format(cs))
        print("count of a:", ca)
        print("count of f:", cf)


co = count_char()
co.get_char()
"3.string slicing"
print("********** One Way ************")
data = "sadsfdgfabaaaasd"
new_data = data[3:10]
print(new_data)
print("********** Second Way ************")
data = "sadsfdgfabaaaasd"
for i in range(len(data)):
    if i >= 3 and i < 10:
        print(data[i], end='')

"4.Python Program to swap the First and the Last Character of a string"
print()
print("************* swap progm***************")
str = "abcde"
newstr = str[-1] + str[1:-1] + str[0]
print(newstr)

str2 = "sangfroid"
newstr_2 = str2[-1] + str2[1:-1] + str2[0]
print(newstr_2)
print("************* Remove odd index in string program***************")
"""Remove odd index value in string data"""
data = "sadsfdgfabaaaasd"
for char in range(len(data)):
    if char % 2 == 0:
        print(data[char], end="")
print()
print("************* count upper and lower char in string program***************")
data = "sad-sfdTRYTTUYgfabaaaasdIUSFHGJUUJ"
COUNTER = 0
counter = 0
for char in data:
    if char >= 'A' and char <= 'Z':
        COUNTER += 1
    if char >= 'a' and char <= 'z':
        counter += 1
print("count of capital char:", COUNTER)
print("count of small char:", counter)

print("**************")
data = "sad-sfdTRY34254435TUYgfabaaaasdI!@*&^%$USFHGJUUJ"
COUNTER = 0
counter = 0
count_digit = 0
count_sp = 0
for char in data:
    if 'A' <= char <= 'Z':
        COUNTER += 1
    elif 'a' <= char <= 'z':
        counter += 1
    elif '0' <= char <= '9':
        count_digit += 1
    else:
        count_sp += 1
print("count of capital char:", COUNTER)
print("count of small char:", counter)
print("count of digit:", count_digit)
print("count of specialchar:", count_sp)

print("**************")
data = "sad-sfdTRY34254435TUYgfabaaaasdI!@*&^%$USFHGJUUJ"
COUNTER = 0
counter = 0
count_digit = 0
count_sp = 0
for char in range(len(data)):
    if data[char].isupper():
        COUNTER += 1
    elif data[char].islower():
        counter += 1
    elif data[char].isdigit():
        count_digit += 1
    else:
        count_sp += 1
print("count of capital char:", COUNTER)
print("count of small char:", counter)
print("count of digit:", count_digit)
print("count of specialchar:", count_sp)

print("***************** convert all alpha to uppercase***********")
data = "sadsfdTRYTTUYgfabaaaasdIUSFHGJUUJ"
for char in data:
    if char.isalpha():
        x = char.upper()
        print(x, end="")

print("***************** convert string in list***********")
data = "sadgfabaaaasdIUUJ"
new_data = list(data)
print(new_data)

print(" count and display vowel in string ")
data = "sad sfdTRYTTUYgfabaaaasdIUSFHGJUUJ"
counter = 0
for char in data:
    if char in '[a,e,i,o,u,A,E,I,O,U]':
        counter += 1
        print(char, end=" ")
print()
print(counter)

print("print first capital latter in string in sentence")
data = "noun is a naming world"
new_data = data.capitalize()
print(new_data)

print("print capitalize the first  latter in each word in given string")
data = "python is an object oriented programming language"
new_data = data.title()
print(new_data)

"print capitalize the first and last latter in each word in given string"
print("*" * 50)
data = "python is an object oriented programming language"
data = data.split()
print(data)
for char in data:
    res = char[0].upper() + char[1:-1] + char[-1].upper()
    print(res, end=" ")
print()
# check if the message starts with Python
message = 'Python is fun'
print(message.startswith('Python'))

s = "python is an oop language"
ind = s.find('python')
print(ind)
ind = s.find('is')
print(ind)
ind = s.find("language")
print(ind)
ind = s.find('k')
print(ind)

s = '1457dataw'
obj = s.isalnum()
print(obj)

s = "hello"
obj = s.isalnum()
print(obj)

s = "hello@*&^"
obj = s.isalnum()
print(obj)

s = "hello world"
obj = s.isalpha()
print(obj)

s = "hello"
obj = s.isalpha()
print(obj)

s = "hello world"
obj = s.isspace()
print(obj)
s = "     "
obj = s.isspace()
print(obj)

s = ["python", ' is', ' an ', 'oop', " language"]
obj = "".join(s)
print(obj)

s = "python is an oop language"
obj = s.split()
print(obj)

s = "python is an oop language"
print("***************** First Way **************")
obj = s.replace("python", "java")
print(obj)
print("*********************** Second Way****************")
s = "python is an oop language"
s1 = s.split()
print(s1)
s1[0] = 'java'
print(s1)
string = " "
for char in s1:
    string += " " + char
print(string, end=" ")
print()
print("**************************************")
s = "python is an oop language"
obj = s.strip()
print(obj)

"Use the format() method to insert numbers into strings:"
age = 36
print("My name is John, and I am {}".format(age))

"program remove newline in python"
str1 = "\n Starbucks has the best coffee \n"
newstr1 = str1.strip()
print(newstr1)

str1 = "\n Starbucks has the best coffee \n"
newstr1 = str1.rstrip()
print(newstr1)

"to print the following floating numbers upto 2 decimal places"
a = 2.154327
print("%0.2f" % a)
a = 2.34865
print("%0.2f" % a)

"Write a Python program to display a number with a comma separator."
x = 3000000
print("Formatted Number with comma separator: " + "{:,}".format(x))
x = 30000000
print("Formatted Number with comma separator: " + "{:,}".format(x))

# to format a number with a percentage
a_number = 1 / 3
percentage = "{:.2%}".format(a_number)
print(percentage)

"swap comma and dot in a string"
amount = "32.054,23"
maketrans = amount.maketrans
result = amount.translate(maketrans('.,', ',.'))
print(result)

"Remove spaces from a given string"
string = "g  eeks  for ge  eeks "
for i in string:
    if i != " ":
        print(i, end="")
print()
print("   second way           ")
string = "g  eeks  for ge  eeks "
result = string.replace(" ", "")
print(result)
"remove leading zeros from an IP address"
