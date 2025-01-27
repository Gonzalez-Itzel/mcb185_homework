# 20demo.py by Itzel Gonzalez
 
# Tuples

t = 1, 2 # this a tuple
print(t)
print(type(t))

person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person)


def midpoint(x1, y1, x2, y2):
	x = (x1 + x2) / 2
	y = (y1 + y2) / 2
	return x, y
print(midpoint(1, 3, 5, 9)) # calls midpoint() fxn and sent to print() fxn

m = midpoint(1, 3 , 5, 9) # assigns the variable m to the return value
print(m)

mx, my = midpoint(10, 7, 8, 5) # unpacks the the tuple
print(mx, my)



# Iteration

'''
while True: 
	print('hello')
'''

i = 0
while True: 
	i = i + 1
	print('hey', i)
	if i == 3: break # once i reaches 3 the loop breaks
	
i = 0
while i < 3: # condition to break loop when no longer true
	i = i + 1
	print('hey', i)
	
i = 0 
while i < 10:
	print(i)
	i = i + 3
	print('final value of i is ', i)
	


# for i in range()

for i in range(1, 10, 3): # initial value, end-before limit and increment
	print(i)

for i in range(0, 5): # increment by one
	print(i)
	
for i in range(5): # give the end-before limit
	print(i) 


# for item in container
# used for iterating over items in a container

basket = 'milk', 'eggs', 'bread' # basket is a tuple
for thing in basket: # steps through basket one at a time
	print(thing)
	
for i in range(len(basket)): 
	print(basket[i])
	

# Nesting

for i in range(7): # range generates a sequence of numbers 
	if i % 2 == 0: print(i, 'is even')
	else: 			print(i, 'is odd')
	


