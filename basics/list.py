# basics
arr=[9,-1,1,2,12,3,4]
arr[1:3]=[1,2]

# methods
arr.remove(1)
del arr[1]
arr.append(3)

for key,item in enumerate(arr):
    print(item,key)

# arr.sort()
print(sorted(arr))

# square of number
print([num ** 2 for num in arr if num >= 2])



