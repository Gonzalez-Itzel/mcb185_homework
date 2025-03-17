import sequence

seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
w = 10 
for i in range(len(seq) -w+1): # prevent window from running off the sequence
	s = seq[i:i+w] # telling it how to move the window
	print(i, s, sequence.gc_comp(s), sequence.gc_skew(s))
	
	
	
	