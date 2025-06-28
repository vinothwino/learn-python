import re
pattern=r'\d+'
str='Vinoth is 28 years old and his friend is 27 years old'

print(re.findall(pattern,str))
print(re.findall(r'[a-zA-Z]+',str))

