# 52kmercount.py by itzel gonzalez

import sys
import mcb185
import itertools

file = (sys.argv[1])
k = int(sys.argv[2])
kcount = {}


for defline , seq in mcb185.read_fasta(file):
	for i in range(len(seq)-k +1): 
		kmer = seq[i:i+k]
		if kmer not in kcount: kcount[kmer] =0 # checks if kmer is in dictinary if not it initializes it
		kcount[kmer] +=1
	for kmer, n in kcount.items(): print(kmer, n) # iterates through the dictionary and prints each unique kmer along with its count

for nts in itertools.product('ACGT', repeat=k): # generates all possible kmers
	kmer = ''.join(nts)
	if kmer in kcount: print( kmer, kcount[kmer]) # checks all possible kmers against kmers
	else: print(kmer,0)