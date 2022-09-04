"""fibonacci series"""
n = 11
first = 0
second = 1
for i in range(n):
    if i <= 1:
        print(i, end=" ")
    else:
        Next = first + second
        print(Next, end=" ")
        first = second
        second = Next
print("\n")


def fibonacci_series(no_term):
    if no_term <= 1:
        return no_term
    else:
        return fibonacci_series(no_term - 2) + fibonacci_series(no_term - 1)


for num in range(11):
    print(fibonacci_series(num), end=" ")
