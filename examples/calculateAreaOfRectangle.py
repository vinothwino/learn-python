def calculate_area(length, width):
 area = length * width
 return area

def get_user_input():
 length = float(input("Enter the length of the rectangle: "))
 width = float(input("Enter the width of the rectangle: "))
 return length, width

def display_result(area):
 print("The area of the rectangle is:", area)

def main():
 length, width = get_user_input()
 area = calculate_area(length, width)
 display_result(area)

main()
