# sequence.py by Itzel Gonzalez

def transcribe(dna):
	return dna.replace ('T', 'U')

def rev.comp(dna):
	rc = [] # holds the new sequence
	for nt in dna[::-1]: # steps backward by 1 
		if nt == 'A': rc.append('T')
		elif nt == 'T': rc.append('A')
		elif nt == 'C': rc.append('G')
		elif nt == 'G': rc.append('C')
		else: 			rc.append('N')
		return ''.join(rc)