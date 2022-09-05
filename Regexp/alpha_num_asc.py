import re


def asc_num(alpha_numeric):
    return list(map(int, re.findall(r'\d+', alpha_numeric)))


lst_data = ['exp45', 'exp123', 'exp21', 'exp27','exp145', 'exp13', 'exp121', 'exp22']
lst_data.sort(key=asc_num)
print(lst_data)


