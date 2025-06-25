t=range(8,2,-1)
min=t[0]
max=t[0]
for num in t:
    if num > max:
        max=num
    if num < max:
        min=num
print(min)
print(max)