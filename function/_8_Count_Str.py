"""accepts a string and calculate the number of upper case letters and lower case letters"""
print(".......................  program 1 .......................")


def lower_upper(string_1):
    count_upper = 0
    count_lower = 0
    for Str in string_1:
        if Str.islower():
            count_lower += 1
        else:
            count_upper += 1
    return f"lower case is : {count_lower}  \n upper case is : {count_upper} \n in string "


str_1 = "sadsfddghhjHBKJHIJIHGBHJHHJ"
print(lower_upper(str_1))

print("........................... Program 2 ..........................")


def Count_String(string_2):
    Count_lower = 0
    Count_upper = 0
    Count_digit = 0
    Count_special = 0
    for char in string_2:
        if char.islower():
            Count_lower += 1
        elif char.isupper():
            Count_upper += 1
        elif char.isdigit():
            Count_digit += 1
        elif char.isspace():
            pass
        else:
            Count_special += 1
    return Count_lower, Count_upper, Count_digit, Count_special


str_2 = "VN2Solution ,Bangalore, 249,sanjeevkrpython@gmail.com"
print(Count_String(str_2))

print("...............................................................")
