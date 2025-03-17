'''goal = 
predict if proteins are transmembrabe by using the proteome data


transmembrane if:
- hydrophobic near the N-terminus
- near other hydrophobic regions'''


import sys 
import mcb185

path = sys.argv[1]

def kd_score(seq):
	h = 0 
	for aa in seq:
		if aa == 'I': h += 4.5
		elif aa == 'V': h += 4.2
		elif aa == 'L': h += 3.8
		elif aa == 'F': h += 2.8
		elif aa == 'C': h += 2.5
		elif aa == 'M': h += 1.9
		elif aa == 'A': h += 1.8
		elif aa == 'G': h -= 0.4
		elif aa == 'T': h -= 0.7
		elif aa == 'S': h -= 0.8
		elif aa == 'W': h -= 0.9
		elif aa == 'Y': h -= 1.3
		elif aa == 'P': h -= 1.6
		elif aa == 'H': h -= 3.2
		elif aa == 'E': h -= 3.5
		elif aa == 'Q': h -= 3.5
		elif aa == 'D': h -= 3.5
		elif aa == 'N': h -= 3.5
		elif aa == 'K': h -= 3.9
		elif aa == 'R': h -= 4.5
	return h/len(seq)

def sig_peptide(seq): # looking for signal peptide in seq
	sig_parameter = seq[:30] # only look at the first 30 aa
	for i in range(len(sig_parameter) - 8 + 1):
		signal = sig_parameter[i:i+8]
		if 'P' in signal: 
			continue
		kd = kd_score(signal)
		if kd >= 2.5:
			return True
	return False 

def trans_membrane(seq):
	sig_parameter = seq[30:]
	for i in range(len(sig_parameter) - 11 + 1):
		trans = sig_parameter[i:i+11]
		if 'P' in trans:
			continue
		kd = kd_score(trans)
		if kd >= 2.0: 
			return True
	return False

for defline, seq in mcb185.read_fasta(path):
	if sig_peptide(seq) == True and trans_membrane(seq) == True:
		print(defline)
	

	
	