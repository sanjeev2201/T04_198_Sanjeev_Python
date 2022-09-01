"""
=>   An Operator is a symbol , which is used to perform certain
     Operations.
=>   If two or more variables / objects connected with an operator then
     it is called  Expression.
=>  In Python Programming, we have 7 types of Operators. They are
    1. Arithmetic Operators: Arithmetic operators are used with numeric values to perform common mathematical operations:
    2. Assignment Operator:   Assignment operators are used to assign values to variables:
    3. Comparison operators:  Comparison operators are used to compare two values:
    4. Logical Operators   :  Logical operators are used to combine conditional statements
    5. Bitwise Operators   :Bitwise operators are used to compare (binary) numbers
    6. Membership Operators :Membership operators are used to test if a sequence is presented in an object
         (a) in
         (b) not in
    7. Identity Operators:   Identity operators are used to compare the objects, not if they are equal,
                             but if they are actually the same object, with the same memory location
         (a) is
         (b) is not

"""

print('.......................  1. Arithmetic Operators    ...........................')
print(" ....................... program 1.1 ....................................")
x = 5
y = 3

print("Addition:", x + y)
print(" ....................... program 1.2 ....................................")
x = 5
y = 3

print("Subtraction:", x - y)

print(" ....................... program 1.3 ....................................")
x = 5
y = 3

print("Multiplication:", x * y)

print(" ........................... program 1.4 ...................................")
x = 12
y = 3

print("Division:", x / y)

print(".................... program 1.5 ...................................")
x = 5
y = 2

print("Modulus:", x % y)

print(' ........................ Program 1.6 ........................... ')
x = 2
y = 5

print("Exponentiation:", x ** y)

print(' ........................ Program 1.7 ........................... ')
x = 15
y = 2

print("floor division:", x // y)

print(' ........................ Program 1.8 ........................... ')
x = 15.0
y = 2

print("floor division:", x // y)

print(' .................................. 2. Assignment Operator .......................... ')
print(' ....................... Program 2.1 ...............................')
x = 5

print(x)

print(' ..................... Program 2.2 ..........................')
x = 5

x += 3

print(x)

print(" ......................... Program 2.3 ..................... ")
x = 5

x -= 3

print(x)

print(" ......................... 3. Comparison operators ...................... ")
print(" ............ program 3.1 ......................... ")
lst = [10, 20, 40, 13, 24, 11]
for i in lst:
    if i > 15:
        print(i, end=" ")
print()
print(" ......................... program 3.2 ..................")
lst_2 = [10, 20, 40, 33, 13, 11, 5]
for i in lst_2:
    if i <= 20:
        print(i, end=" ")
print()
print(" ......................... program 3.3 ..................")
lst_3 = [10, 20, 40, 33, 13, 11, 5, 20, 20]
for i in lst_3:
    if i != 20:
        print(i, end=" ")
print()
print("..................... 4. Logical Operators ...............")
print(" ......................... program 4.1 .................. ")
lst_4 = [10, 20, 40, 13, 24, 11]
for i in lst_4:
    if 9 < i <= 15:
        print(i, end=" ")
print("....................... program 4.2 ........................")
lst_5 = [10, 20, 40, 33, 13, 11, 5, 20, 20]
for i in lst_5:
    if i >= 10 and i <= 20:
        print(i, end=" ")

print("........................ 5. Bitwise Operators ........................")
print("................. Program 5.1 .......................")
a = 10
b = 20
print(a | b)

print("................... Program 5.2 ........................")
a = 10
b = 20
print(a & b)

print("................... Program 5.3 ........................")
a = 10
b = 20
print(a ^ b)
print('......................... 6. Membership Operators .....................')
print("...................Program 1 ..................")
Str_1 = "ewsrdfyhiojknjbhjRETRRFYGFVHKLJNMGHFCRES"
Vowel = "[a,e,i,o,u,A,E,I,O,U]"
Count_Vowel = 0
for char in Str_1:
    if char in Vowel:
        Count_Vowel += 1
print("Number of Vowel in String:", Count_Vowel)

print("...................Program 2 ..................")
Str_2 = "ewsrdfyhiojknjbhjRETRRFYGFVHKLJNMGHFCRES"
Vowel = "[a,e,i,o,u,A,E,I,O,U]"
Count_Cons = 0
for char in Str_2:
    if char not in Vowel:
        Count_Cons += 1
print("Number of Consonant in String:", Count_Cons)

print("............................. 7.Identity Operators .................... ")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print("addr x:", id(x))
print("addr y:", id(y))
print("addr z:", id(z))
print("......................... program 1 ..................................")
print(x is z, ':Because addr is  Same')
print(x is y, ':Because addr is not Same')

print(".................. Program 2 .........................")
lst_6 = [10, 20, 30, 40, 50]
lst_7 = [10, 20, 30, 40, 50]
print("addr lst_6:", id(lst_6))
print("Addr lst_7:", id(lst_7))
print(lst_6 is lst_7, 'Because Addr is not Same')
print(lst_6 == lst_7, 'Because Values is S  Same')

