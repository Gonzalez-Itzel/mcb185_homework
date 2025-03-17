# 45colorname.py by Itzel Gonzalez

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

mini_diff = 255 # initializing the minimum color by the maximum color

def dtc(P1, P2): # P1 (3 #s) is from the command line and P2 is from the color file
	d = 0
	for p1, p2 in zip(P1, P2): # we are comparing three numbers at a time
		d = d + abs(p1-p2) # summing all three numbers between the three numbers 
	return d 


with open(colorfile) as fp:
	for line in fp:
		words = line.split() 
		colorname = words[0]
		colorvals = words[2] # this extracts the numbers from the file
		
		vals = []
		for i in colorvals.split(','): #all three numbers are seperated by commas
			vals.append(int(i)) # turns the strings into actual numbers
		
		x = [R, G, B] # it holds all three numbers from the command the line
		diff = dtc(x, vals)  
				
		if diff < mini_diff: # going through the loop and comparing the difference to the diff_mini
			diff = mini_diff
			target_color = colorname # extracts the color name
print(colorname)
			
			
		
		
	
	
	
	
		

		
		