# 35scoringmatrix.py by Itzel Gonzalez
import sys

seq = sys.argv[1]
match_score = sys.argv[2]
mismatch_score = sys.argv[3]

print("   " + "  ".join(seq))

for i in range(0, len(seq)):
    print(seq[i], end=" ")  
    for j in range(0, len(seq)): 
        if seq[i] == seq[j]: 
            print(f"{match_score:>2}", end=" ") 
        else:
            print(f"{mismatch_score:>2}", end=" ")  
    print() 

# assessment without using no range, no f strings, and no join
print("   ", end='')
for nt in seq:
	print(nt, end="  ")
print()

for nt1 in seq:
	print(nt1, end= " ")
	for nt2 in seq:
		if nt1 == nt2: print(match_score, end=' ')
		else: print(mismatch_score, end=' ')
	print()
	


	


	


	
























