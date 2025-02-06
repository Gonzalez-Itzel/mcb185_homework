import math 

# Always start with a smaller limit and work your way up to ensure that it works

limit = 100 # determines the limit of variable 'a' and 'b'


for a in range(1, limit):
	for b in range (1, limit):
	 	c = math.sqrt(a**2 + b**2)
	 	remainder = c % 1
	 	if remainder  == 0: print(a, b, c)
		
