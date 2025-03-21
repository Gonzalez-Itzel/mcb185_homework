# 55genefinder by Itzel and Livleen

import sys
import mcb185
import sequence

file = sys.argv[1]
min_orf_length = int(sys.argv[2])


def cds_finder(seq, length_of_aas):

    tranlsated_proteins = []

    aas = mcb185.translate(seq)

    orfs = aas.split('*')

    for orf in orfs:
        if 'M' in orf:
            start = orf.find('M')
            protein = orf[start:]

            nt_seq = seq[:len(protein) * 3]

            if len(nt_seq) >= min_orf_length:
                tranlsated_proteins.append(nt_seq)

    return tranlsated_proteins 



for defline, seq in mcb185.read_fasta(file):
	words = defline.split()
	identifier = words[0]
	seq_num = 0
	reverse_strand = mcb185.anti_seq(seq)

	for frame in range(3):
		position = 0 
		while position < len(seq) - frame: 
			forward_orfs = cds_finder(seq[frame:], min_orf_length)
			for forward in forward_orfs:
				seq_num += 1
				start_position = position + frame
				end_position = start_position + len(forward)
				print(identifier, "CDS", start_position, end_position, seq_num, "+")
				position += len(forward)

	for frame in range(3):
		position = 0 
		while position < len(reverse_strand) - frame: 
			reverse_orfs = cds_finder(reverse_strand[frame:], min_orf_length)
			for reverse in reverse_orfs:
				seq_num += 1
				start_position = position + frame
				end_position = start_position + len(reverse)
				print(identifier, "CDS", start_position, end_position, seq_num, "-")
				position += len(reverse)