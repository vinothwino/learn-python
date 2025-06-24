def count_vowels(str):
    VOWELS='aeiouAEIOU'
    vowels_count=0;
    for char in str:
        if char in VOWELS:
            vowels_count+=1
    return vowels_count

def main():
    str=input('Enter the vowels: ')
    print(f'Vowels count is: {count_vowels(str)}')

main()