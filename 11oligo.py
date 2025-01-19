# 11oligo.py by Itzel Gonzalez


def oligo_mt(A, T, C, G):
	if (A + T + C + G) <= 13:
		return (A + T) * 2 + (G + C) * 4 
	else: # for longer oligos
		return 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)

print(oligo_mt(4, 5, 9, 2))
print(oligo_mt(3, 2, 3, 4))
print(oligo_mt(12, 15, 22, 24))
