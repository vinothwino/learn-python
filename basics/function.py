## basic 

# def square(x):
#  result = x ** 2
#  return result
# square_result = square(5)
# print(square_result)

## with argument

# def multiple(a,b):
#     return a*b

# keyword argument
# print(multiple(b=12,a=4))

# variable length argument

# def add_numbers(*args):
#     return sum(args)

# print(add_numbers(12,24,5))

# def multiply_numbers(*kwargs):
#     result=0;
#     for key, value in kwargs.items():
#         result+=value
#     return result


# print(multiply_numbers(a=12,n=5,c=11))

## call by assignment

# def update_userId(id):
#     id= f'# {id}'
# id = 123
# print("Before the function call:", id)
# update_userId(id)
# print("After the function call:", id)

## call by object reference

# def modify_list(lst):
#  lst.append(4)
#  lst[0] = "Modified"
# my_list = [1, 2, 3]
# print("Before the function call:", my_list)
# modify_list(my_list)
# print("After the function call:", my_list)

## nested function

def outer_function(x):
 def inner_function(y):
    return x + y
 result = inner_function(5)
 return result
output = outer_function(3)
print("Output:", output)
