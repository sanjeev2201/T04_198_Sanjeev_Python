"""
A variable name must begin with a letter of the alphabet or an underscore(_)
Example: abc=100 #valid syntax. ...
(i) The first character can be followed by letters, numbers or underscores. ...
(ii) Python variable names are case sensitive. ...
(iii)Reserved words cannot be used as variable names.
"""

"""Global and Local Python Variables in python
Local Variables
.................
Local variables are the ones that are defined and declared inside a function.
 We can not call this variable outside the function.
 
Global Variables
..................
Global variables are the ones that are defined and declared outside a function,
 and we need to use them inside a function.
"""

print("...................  program 1...................")


def f():
    S = "Welcome Sanjeev"
    print(S)


f()

print(".......................... Program 2 ........................")


# This function has a variable with
# name same as s.
def f():
    print(s)


# Global scope
s = "I love Python"
f()

"""
Global keyword in Python
.........................
Global keyword is used inside a function only when we want to do assignments or
 when we want to change a variable.
"""
print("...................... program 3............................................")
# Python program to modify a global
# value inside a function

x = 15


def change():
    # using a global keyword
    global x

    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :{}".format(x))


change()
print("Value of x outside a function :{}".format(x))

print("....................... Program 4 .............................")


def f():
    global s
    print(s)
    s = "Only in spring, but Bangalore is great as well!"
    print(s)


Str = "I am looking for a course in India!"
f()
print(s)

print(".............................. Program 5 .........................")


def foo(X, Y):
    global a
    a = 42
    X, Y = Y, X
    b = 33
    b = 17
    c = 100
    print(a, b, X, Y)


a, b, x, y = 1, 15, 3, 4
foo(17, 4)
print(a, b, x, y)
