import math 

# Always start with a smaller limit and work your way up to ensure that it works

limit = 100 # determines the limit of variable 'a' and 'b'


for a in range(1, limit): # side a triangle
	for b in range (1, limit): # side b of a triangle
	 	c = math.sqrt(a**2 + b**2)
	 	remainder = c % 1 # we want only integer
	 	if remainder  == 0: print(a, b, c) # if there is no remainder, it is an integer
		
