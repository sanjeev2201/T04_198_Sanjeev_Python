""" To check armstrong Number """
print("..............................1. Program .....................")
n = 153
x = n
power = len(str(n))
new_number = 0
while n > 0:
    r = n % 10
    new_number = new_number + r ** power
    n = n // 10
if new_number == x:
    print("Number is  Armstrong Number:{}".format(x))
else:
    print("Number is   not Armstrong Number:{}".format(x))

print("................................ 2. Program ..........................")


def Armstrong(Number):
    for nm in Number:
        old_Number = nm
        length = len(str(nm))
        New_no = 0
        while nm > 0:
            rem = nm % 10
            New_no += rem ** length
            nm = nm // 10
        if New_no == old_Number:
            print("Number is Armstrong:", old_Number)
        else:
            print("Number is not Armstrong:", old_Number)


List_data = [154, 133, 126, 186, 153]
Armstrong(List_data)

"""
Q. Check Armstrong Number in range(1,1001)
"""
print("......................Program 3......................")
for nm in range(11, 1001):
    x = nm
    length = len(str(nm))
    arm_no = 0
    while nm > 0:
        rem = nm % 10
        arm_no += rem ** length
        nm = nm // 10

    if x == arm_no:
        print("Armstrong Number is :{}".format(x))
