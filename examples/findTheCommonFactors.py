set1={1, 2, 3, 4, 6, 12}
set2={1, 2, 4, 8, 16}

common_factors=[]

for num in set1:
    if all(num1 % num == 0 for num1 in set2):
        common_factors.append(num)

print(set1 & set2)