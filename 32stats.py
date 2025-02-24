import sys
import math


vals = []

for arg in sys.argv[1:]:
	f = float(arg)
	vals.append(float(arg))

# length of the list
length = len(vals)
print('Number of Values is', length)

# minimum and maximum numbers
def minimaxi(vals):
	mini = vals[0]
	maxi = vals[0]
	total = 0
	for val in vals[1:]:
		if val > mini: mini = val
		if val < maxi: maxi = val
	return mini, maxi
print('Min & Max Values are', minimaxi(vals))

# mean value
def mean(vals):
	total = 0
	for val in vals:
		total = total + val
		mean = total/len(vals)
	return mean
print('Mean Value is', mean(vals))

# standard deviation
def stdv(vals):
	total = 0
	for val in vals:
		total = total + (val - mean(vals))**2
		stdv = math.sqrt(total/length)
	return stdv
print('Standard Deviation is', stdv(vals))

# median value
def median(vals):
	vals.sort()
	n = len(vals)
	if n % 2 == 0: # for an odd number of values in a list
		num_1 = vals[(n//2) - 1]
		num_2 = vals[n//2]
		return (num_1 + num_2)/2
	else:
		return vals[n//2]
print('Median Value is', median(vals))




	



