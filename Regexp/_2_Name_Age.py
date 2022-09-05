import re

gd = """
   Janice is 22 and Theron is 22
   Gabriel is 44 and Jones is 100
    """
name = re.findall(r'[A-Z][a-z]+', gd)
age = re.findall(r'\d{1,3}', gd)
dict_data = {}
for nm in name:
    for ag in age:
        dict_data[nm] = int(ag)
        age.remove(ag)
        break
print(dict_data)
