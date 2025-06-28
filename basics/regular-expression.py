import re

# basic methods
pattern=re.compile('vinoth')
str="The vinoth working as UI developer, vinoth is an reliable engineer"
if(re.match(pattern,str)):
    print('Match found')
else:
    print('Match not found') # output match not found
if(re.search(pattern,str)):
    print('Match found') # found
else:
    print('Match not found')
if(re.findall(pattern,str)):
    print('Match found',re.findall(pattern,str)) # found
else:
    print('Match not found')

print(re.split(' ',str,maxsplit=2),'splitted') # split the string based on space added






