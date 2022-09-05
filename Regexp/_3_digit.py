from re import findall

str = "one two three four five six seven 8 9 10 1112 hundred"
result = findall(r'\b\d+\b', str)
print(result)
