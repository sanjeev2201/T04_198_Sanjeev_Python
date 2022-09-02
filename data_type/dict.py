print("......................... dictionary  ........................")
print("..................... 1.program ...........................")
"""Add a key to a dictionary """
dict_data_1 = {}
dict_data_1['a'] = 100
dict_data_1['b'] = 200
dict_data_1['c'] = 300
dict_data_1['d'] = 400
print(dict_data_1)

print(" ............................. 2. Program ..............................")
"Check if a given key already exists in a dictionary."
Dic_data_2 = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
result = False
for keys in Dic_data_2.keys():
    if 'd' in keys:
        result = True
        break
if result:
    print(" d key is present in dictionary data")
else:
    print(" d key is not present in dictionary data")

print(" ......................... 3.Program ...................")
"Merge two Python dictionaries"
print(" .................... Method 1 ....................")
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
res = dict1 | dict2
print("Merge two dictionary:", res)

print("......................... Method 2 ..........................")
dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict1.update(dict2)
print("Merge two dictionary:", dict1)

print(".................... 4.Program ................ ")
"Sum all the items in a dictionary"
dic_sum_val = {'a': 100, 'b': 200, 'c': 300}
Sum = 0
for value in dic_sum_val.values():
    Sum += value
print("sum of value in dictionary:", Sum)

dic_sum_val = {'a': 400, 'b': 500, 'c': 600}
Sum = 0
for value in dic_sum_val:
    Sum += dic_sum_val[value]
print("sum of value in dictionary:", Sum)

print(".......................... 5.Program ........................")
"Multiply all the items in a dictionary"
dict_data_2 = {'value1': 5, 'value2': 4, 'value3': 3, 'value4': 2, 'value5': 1}
mul_val = 1
for key in dict_data_2:
    mul_val = mul_val * dict_data_2[key]
print("Multiply all the values in Items:", mul_val)

print(".................... 6. Program ........................")
"Get the maximum and minimum value in a dictionary.	"
dict_data_3 = {"Oliva": 18, "potter": 56, "Harry": 15}
New_list = []
for key in dict_data_3:
    New_list.append(dict_data_3[key])
Max_Val = New_list[0]
for val in New_list:
    if val > Max_Val:
        Max_Val = val
print("Maximum Value in Dictionary :", Max_Val)
Min_Val = New_list[0]
for val in New_list:
    if val < Min_Val:
        Min_Val = val
print(" Minimum Value in Dictionary :", Min_Val)

print("..................... 7.Program ....................")
"Remove duplicates from Dictionary"
Rm_dup_dict = {'gfg': 10, 'is': 15, 'best': 20, 'for': 10, 'geeks': 20}
list_1 = []
New_Dict = {}
for key in Rm_dup_dict:
    if Rm_dup_dict[key] not in list_1:
        list_1.append(Rm_dup_dict[key])
        New_Dict[key] = Rm_dup_dict[key]
print("New Dict:", New_Dict)

print(".......................... 8. Program .......................")
"Combine two dictionary adding values for common keys."
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}
for key1 in dict1:
    if key1 in dict2:
        dict1[key1] = dict1[key1] + dict2[key1]
print("Combine addition value for common Key:", dict1)

print("Create a dictionary from a string. ")
String_data = "wryyijbczzryookkvhghjk4324546688"
dict_data_4 = {}
for char in String_data:
    dict_data_4[char] = dict_data_4.get(char, 0) + 1
print(dict_data_4)

print("....................... 9.Program .............................. ")
"Map two lists into a dictionary"
key = ['a', 'b', 'c', 'd', 'e']
val = [100, 200, 300, 400, 500]
dict_data_5 = {}
for i in key:
    for j in val:
        dict_data_5[i] = j
        val.remove(j)
        break
print(dict_data_5)

key_1 = ['a', 'b', 'c', 'd', 'e']
val_1 = [100, 200, 300, 400, 500]
dict_data_6 = {}
for i in key_1:
    for j in val_1[::-1]:
        dict_data_6[i] = j
        val_1.remove(j)
        break
print(dict_data_6)

print(" ........................... 10. Program .........................")
"Convert a list into a nested dictionary of keys. "
l1 = ['a', 'b', 'c', 'd']
l2 = ['e', 'f', 'g', 'g']
l3 = [10, 20, 30, 40]

Nested_dict = [{a: {b: c}} for a, b, c in zip(l1, l2, l3)]
print("Nested Dictionary :", Nested_dict)
print(" ............................. 11. Program .................................")
Nested_list = [['Sachin', 348], ['Dhoni', 383], ['Kohli', 379], ['Gautam', 401]]
Conv_Dict = {}
for val in Nested_list:
    Conv_Dict[val[0]] = val[1]
print("Convert Nested list into dict :", Conv_Dict)
