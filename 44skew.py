# 44skew.py 

import sequence
import sys 
import mcb185

file = sys.argv[1]
w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(file):
	window = seq[:w]
	gc_initial = window.count('G') + window.count('C')
	g_initial = window.count('G')
	c_initial = window.count('C')
	
	for i in range(1, len(seq) - w + 1):
		old_nt = seq[i-1]
		if old_nt == 'G':
			gc_initial -= 1
			g_initial -= 1
		elif old_nt == 'C':
			gc_initial -= 1
			c_initial -= 1
		
		new_nt = seq[i + w - 1]
		if new_nt == 'G':
			gc_initial += 1
			g_initial += 1
		elif new_nt == 'C':
			gc_initial += 1
			c_initial += 1
	
		print(i, sequence.gc_comp(seq[i:i+w]), sequence.gc_skew(seq[i:i+w]))
		
	
		
	
	sequence.gc_comp(seq)