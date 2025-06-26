#define

obj={"name":'ganesh'}

obj=dict([['name','ganesh']])

# access

obj["name"]

obj.get('name')

# add

obj['age']=28

# remove

del obj['age']

obj.pop('age','not found')
obj.popitem('age')

# copy

obj1=obj.copy()

# utils

obj.values()

obj.items()

obj.keys()