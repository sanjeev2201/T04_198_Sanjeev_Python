print("...................... Program 1 ..........................")
# logic 5!=1*2*3*4*5
n = 5
fact = 1
for i in range(1, n + 1):
    fact = fact * i
print(f"factorial of 5 :{fact}")

print(" factorial of list of data by using function")


def factorial(data):
    # business logic
    for fac in data:
        factor = 1
        for j in range(1, fac + 1):
            factor = factor * j
        print(f"factorial of {fac} is: {factor}")


lst = [5, 7, 6, 4]
factorial(lst)


def factorial_recursion(n):
    if n ==1:
        return n
    else:
        return n*factorial_recursion(n-1)
number = 5
print(factorial_recursion(number))