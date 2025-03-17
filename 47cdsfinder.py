import sys 
import mcb185

file = sys.argv[1]
aa_length = int(sys.argv[2])




def find_orfs(seq, aa_length):
	translated_proteins = []
	
	pro_seq = mcb185.translate(seq)
	
	orfs = pro_seq.split('*')
	
	for orf in orfs:
		if 'M' in orf:
			start = orf.find('M')
			protein = orf[start:]
			
			if len(protein)	>= aa_length:
				translated_proteins.append(protein)
	
	return translated_proteins
	
for defline, seq in mcb185.read_fasta(file):
	words = defline.split()
	identifier = words[0]
	seq_num = 0
	reverse_strand = mcb185.anti_seq(seq)
	
	for frame in range(3):
		for forward in find_orfs(seq[frame:], aa_length):
			seq_num += 1
			print('>',identifier, "-proto-", seq_num, sep='')
			print(forward)
	
		for reverse in find_orfs(reverse_strand[frame:], aa_length):
			seq_num += 1
			print('>',identifier, "-proto-", seq_num, sep='')
			print(reverse)
	