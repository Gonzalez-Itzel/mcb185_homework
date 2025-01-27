# 12phred.py by Itzel Gonzalez

'''
Write functions that convert quality value symbols into error rates and vice-versa. 
The ord() function returns the ASCII value of a letter. The chr() function turns an ASCII value 
into a letter
'''

import math

def qsymbol_to_error_rate(x):
	phred = ord(x) - 33
	p = 10 ** (-phred/10)
	return p
	
print(qsymbol_to_error_rate('A'))

def error_rate_to_qsymbol(y):
	q = -10 * math.log10(y) 
	return chr(int(q + 33))

print(error_rate_to_qsymbol(0.316))
	
	
	





