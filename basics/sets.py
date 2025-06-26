# define

fruits = {"apple", "banana", "orange"}

fruits = set(["apple", "banana", "orange"])

# add

fruits.add('grapes')

# remove

fruits.remove('apple')

# update

fruits.update({'apple'})

# discard 

fruits.discard('apple') # dont throw error when item is not present

# union

fruits.union({"gaming"})

# intersection

fruits.intersection({"banana"})

# difference

fruits.difference({"banana"})

# symmmetric diff
fruits.symmetric_difference({"gaming"})

# clear

fruits.clear()