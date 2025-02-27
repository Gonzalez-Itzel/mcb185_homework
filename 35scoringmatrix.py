# 35scoringmatrix.py by Itzel Gonzalez
import sys

seq_1 = sys.argv[1]
seq_2 = sys.argv[1] 
match_score = int(sys.argv[2])
mismatch_score = int(sys.argv[3])

print("   " + "  ".join(seq_2))

for i in range(0, len(seq_1)):
    print(seq_1[i], end=" ")  
    for j in range(0, len(seq_2)): 
        if seq_1[i] == seq_2[j]: 
            print(f"{match_score:>2}", end=" ") 
        else:
            print(f"{mismatch_score:>2}", end=" ")  
    print()  




















