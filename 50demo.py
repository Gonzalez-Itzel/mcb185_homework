# sets 
s = {'A', 'C', 'G'}
print(s) # changes order every time you run it

s.add('T')
print(s) # adds T to the set

s.add('A') # doesn't do anything bc A is already in the list
print(s)

# print(s[2]) will give error bc sets are not numerical indexes

# dictionaries

d = {} # technique 1 
d = dict() # technique 2

d = {'dog': 'woof', 'cat': 'meow'}
print(d)
print(d['cat']) # to access items in square brackets

d['pig'] = 'oink' # add new items, assign a new key:value pair
print(d)

d['cat'] = 'mew' # to change the value of an item
print(d)

del d['cat'] # delete an item
print(d)

if 'dog' in d: print(d['dog']) # to check if a key exists, use 'in

# iteration
# format
# for key in d: print(f'{key} says {d[key]}')

for k, v in d.items(): print(k, 'says', v) # most common way to iterate through a dictionary

print(d.keys(), d.values(), list(d.values())) # prints dict_keys(), dict_values, list of values in d
