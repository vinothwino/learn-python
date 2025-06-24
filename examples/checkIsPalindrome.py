def isPalindrome():
    str=input('Enter the word to check palidrome:')
    reverseStr=str[::-1]
    isTextPalindrome= str==reverseStr;
    return isTextPalindrome

print(isPalindrome())