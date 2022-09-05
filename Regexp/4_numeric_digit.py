import re

str = 'The meeting will be conducted on 1st and 21st of every month'
result = re.findall(r'\d[\w]+', str)
print(type(result))
print(result)
