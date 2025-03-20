'''
parser = argparse.ArgumentParser(description = 'DNA entroppy filter.') # creates a helper that explains what the program does  
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20, help='window size[%(default)i]') # if user doesnt provide size, the default window size is 20
parser.add_argument('--entropy', type=float, default=1.4, help='entropy threshold [%(default).3f]') # [%(default).3f] uses 3 digits of precision, f= float
arg = parser.parse_args() # reads the user inputs


# -- you are telling the program what value to use for either the window size or entropy rather than default

#print('dusting with', arg.file, arg.size, arg.entropy)
#print('dusting with', arg.file, arg.size, arg.entropy, sep='\t', end='\n') # order does not matter
#print('dusting with', arg.file, arg.size, arg.entropy, end='\n', sep='\t') # order does not matter because they are named arguments


# flags turn on/off some behavior
parser = argparse.ArgumentParser(description = 'DNA entroppy filter.')  
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('--size', type=int, default=20, help='window size[%(default)i]') 
parser.add_argument('--entropy', type=float, default=1.4, help='entropy threshold [%(default).3f]') 
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args() 
print('dusting with', arg.file, arg.size, arg.entropy, arg.lower)

# ability to use both short an long names

parser.add_argument('-s','--size', type=int, default=20, help='window size[%(default)i]') 
parser.add_argument('e', '--entropy', type=float, default=1.4, help='entropy threshold [%(default).3f]') 
'''

import math
import sys
import mcb185
import argparse  # helps understand user input


def entropy(window):
	a = window.count('A') / len(window)
	c = window.count('C') / len(window)
	g = window.count('G') / len(window)
	t = window.count('T') / len(window)
	
	H = 0
	for prob in [a, c, g, t]:
		if prob > 0:
			H -= prob * math.log2(prob)
	
	return H

parser = argparse.ArgumentParser(description = 'DNA entroppy filter.')  
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s','--size', type=int, default=20, help='window size[%(default)i]') 
parser.add_argument('-e','--entropy', type=float, default=1.4, help='entropy threshold [%(default).3f]') 
parser.add_argument('--lower', action='store_true', help='soft mask')
parser.add_argument('--wrap', type=int, default=60, help='wrap size')
arg = parser.parse_args() 


for defline, seq in mcb185.read_fasta(arg.file):
	mask = list(seq) # from class	
	for i in range(len(seq) - arg.size + 1):
		window = seq[i:i+arg.size]
		if entropy(window) < arg.entropy: 
			for j in range(i, i+arg.size):
				if arg.lower: mask[j] = 'N'
			
	print(defline)
	
	for i in range(0, len(mask), arg.wrap):
		print(''.join(mask[i:i+arg.wrap]))
