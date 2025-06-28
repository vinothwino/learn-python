orig_num=int(input('Enter the number to check palindrome'))
num=orig_num
reverse=0

while (num > 0):
    digit=num%10
    reverse=reverse*10+digit
    num//=10

if orig_num == reverse:
    print('It a palindrome')
else:
    print ('It is not a palindrome')
