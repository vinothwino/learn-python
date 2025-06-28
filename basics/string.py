# string

# slicing
str='vinoth kumar'
print(str[0:6]) #vinoth
print(str[7:12]) #kumar
print(str[::2]) # increment by 2

# printing string using format method

print ('{0} {1}'.format('vinoth','kumar'))
print ('{firstName} {lastName}'.format(firstName='vinoth',lastName='kumar'))
print({'name'})

# escape sequence

print('vinoth\'s story')
print('vinoth\'s story')
print('''vinoth's story''')
print('vinoth\tkumar')
print('vinoth\nkumar')

# methods
str='vinoth kumar'
len(str) #12
f'{str}  '.strip() # remove white space
f'  {str} '.lstrip() # vinoth D
f'  {str} '.lstrip() # vinoth D
str.split()
str.index('v')
str.find('v') # return -1 if element not found
str.count('v')
'john is very shy. Jenny being friendly with john to comfort him'.replace('john','Abraham') # replace all occurance
str.join('loves coding')

str.upper()
str.lower()
str.capitalize()
str.casefold() # make it caseless

# type casting 

int(str)
str(123) 
chr(97) # a
ord('a') #97
