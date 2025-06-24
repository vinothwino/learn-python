def calculateFactorial(num):
    result=1
    for i in range(1,num+1):
        result*=i;
    return result

def main():
    num=5;
    print(f'Factorial of {num} is {calculateFactorial(num)}')
main()