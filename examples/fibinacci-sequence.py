def generate_fibonacci_sequence():
    fibonacci_sequence = [0, 1]
    count = 2
    while count < 10: # Generate the first 10 numbers in the Fibonacci sequence
        next_number = fibonacci_sequence[count - 1] +fibonacci_sequence[count - 2]
        fibonacci_sequence.append(next_number)
        count += 1
    return fibonacci_sequence

def display_result(sequence):
 print("Fibonacci Sequence:", sequence)
 
def main():
 fibonacci_sequence = generate_fibonacci_sequence()
 display_result(fibonacci_sequence)
main()
