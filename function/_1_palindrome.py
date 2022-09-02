def palindrome(nm):
    new_nm = nm[::-1]
    if nm.lower() == new_nm.lower():
        print(f"{nm} is palindrome")
    else:
        print(f"{nm} is not Palindrome")


name_1 = "Madam"
palindrome(name_1)
name_2 = "Mom"
palindrome(name_2)
name_3 = "Sachin"
palindrome(name_3)

print("************************ program 2 ***********************")


def Check_Pal(number):
    x = number
    rev_no = 0
    while number != 0:
        r = number % 10
        rev_no = rev_no * 10 + r
        number = number // 10
    print(rev_no)
    if x == rev_no:
        return "number is Palindrome"
    else:
        return "Number is not palindrome"


no_1 = 144
print(Check_Pal(no_1))
no_2 = 121
print(Check_Pal(no_2))
