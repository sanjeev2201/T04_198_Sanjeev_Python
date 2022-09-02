def prime_number(n):
    for i in n:
        result = False
        for j in range(2, i):
            if i % j == 0:
                result = True
                break
        if result:
            print("Number is not prime:", i)
        else:
            print("Number is  prime:", i)


# function call
lst = [3, 7, 21, 16, 31]
prime_number(lst)

"Count Number of Prime Number in given List"


def Count_Prime(data):
    count = 0
    for val in data:
        for j in range(2, val):
            if val % j == 0:
                break
        else:
            count += 1
            print(count, "       ", val)


lst = [3, 7, 21, 16, 31]
print("count      Number")
Count_Prime(lst)
