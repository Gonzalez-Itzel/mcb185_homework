'''
Write a program that searches sequences for the smallest missing k-mer.
Start k at 1 and increase until there are missing k-mers
Only report the k-mers that are missing
Stop after finding a value of k with missing k-mers
Search both strands of the sequence 
The output of your program should find 52 missing k-mers in the E.coli genome at k=8.
'''
# 54missingkmers.py by Itzel and Livleen

import sys
import mcb185 #using it for anti_seq
import itertools

file = (sys.argv[1])
kcount = {} # ex. ATCG:1, AATC: 2
missing_kmers = [] # keeps tracks of missing kmers
n = 0 

for k in range(1, 10):
kcount = {} # ex. ATCG:1, AATC: 2
	for defline , seq in mcb185.read_fasta(file):
		rev_seq = mcb185.anti_seq(seq)
		strands = {'f_strand': seq, 'r_strand': rev_seq}
		
		for strand_type, strand in strands.items(): 
			for i in range(len(strand)- k + 1): 
				kmer = strand[i:i+k]
				if kmer not in kcount:
					kcount[kmer] = 0 # checks if kmer is in dictinary if not it initializes it
				kcount[kmer] +=1
	
	if len(kcount) == 4**k: continue
	for nts in itertools.product('ACGT', repeat=k): # generates all possible kmers
		kmer = ''.join(nts)
		if kmer not in kcount: print(kmer)
	break
