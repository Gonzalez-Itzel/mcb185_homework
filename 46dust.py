# 46dust.py by Itzel Gonzalez
import math
import sys
import mcb185

file = sys.argv[1]
w = 4
entropy_thresh = 1.4
wrap = 60

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


	
for defline, seq in mcb185.read_fasta(file):
	mask = list(seq)
	
	for i in range(len(seq) - w + 1):
		window = seq[i:i+w]
		if entropy(window) < entropy_thresh: 
			for j in range(i, i+w):
				mask[j] = 'N'
			
	print(defline)
	
	for i in range(0, len(mask), wrap):
		print(''.join(mask[i:i+wrap]))

		
			