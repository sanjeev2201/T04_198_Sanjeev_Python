list_data = [10, 40, 35, 14, 22, 27]
Sum = 0
for val in list_data:
    Sum += val
print(f"Sum of Number:{Sum}")

print("............... sum of data using function ..........................")


def Sum_List_Data(data):
    sum_val = 0
    for Val in data:
        sum_val += Val
    return f"Sum of value is:{sum_val}"


list_value = [10, 40, 35, 14, 22, 27]
print(Sum_List_Data(list_value))
