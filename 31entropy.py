# 31entropy.py by Itzel Gonzalez
import sys
import math

probs = []  # sets up container
for arg in sys.argv[1:]: # skips over the name of the program
	f = float(arg) # turns argument into floating point
	if f <= 0 or f >=1: sys.exit('error: not a probability')
	probs.append(float(arg)) # adds each floating point number to container

total = 0 
for p in probs: total += p
if not math.isclose(total, 1.0): 
	sys.exit('error: probs must sum to 1.0')

h = 0 
for p in probs:
	h -= p *math.log2(p)

print(f'{h:.4f}')