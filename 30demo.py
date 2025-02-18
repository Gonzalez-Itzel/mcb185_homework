y = 'hello world'
print(y)

y1 = 'hey "dude"'
y2 = "don't tell me what to do"
print(y1, y2)
print('hey "dude" don\'t tell me what to do')

a = 'hello' + 'world'
polyA = 'A' * 100
print(a)
print(polyA)


# String Functions
s = 'ATCGTGACCGATACGA'
print(len(s)) # get the length of a string

print(chr(65)) # get character whose ASCII value is n

print(ord('$')) # get ASCII value of character c

# Method Syntax
print(s.lower()) # function name comes first followed by method syntax
print(s)

print(y.replace('o', '')) # o is replaced by an empty string
print(y.replace('o', '').replace('r', 'i')) # o is replaced by an empty string, followed by r being replaced by an i


# f strings (modern method)
# allows you to embed expressions inside a string 
import math 

print(f'{math.pi}') # does nothing
print(f'{math.pi:.3f}') # 3 fixed digits after the decimal
print(f'{1e6 * math.pi:e}') # exponent notation
print(f'{"hello world": >20}') # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:10} {10}') # left justify

# Indexes
seq = 'GAATTC'
print(seq[0], seq[1]) # extracts character
print(seq[-1]) # count backwards from the right (last character of a string)

for nt in seq: # prints the nucleotides in seq with spaces in b/n
	print(nt, end=" ")
print()


# 'for i in range' means you are going to do something n times 
for i in range(len(seq)): # will give the position of nt in the sequence length
	print(i, seq[i]) # prints the number/position, nt in that position
	

# Slices 
s = 'ABCDEFGHIJ'
print(s[0:5]) # extracts characters from index 0 to 4
print(s[0:8:2]) # slices 0 through 8 with a step size of 2
print(s[0:5], s[:5]) # both syntax are the same and result in ABCDE
print(s[5:len(s)], s[5:]) # from position 5, lists the length of the string FGHIJ
print(s)  # prints string name
print(s[::]) # prints string from beginning to end
print(s[::1]) # prints string one character at a time, step of 1
print(s[::-1]) # prints string in reverse order

dna = 'ATGCTGTAA'
for i in range (0, len(dna), 3): # move in steps of 3
	codon = dna [i: i + 3] # take 3 letters
	print(i, codon) 
	
# Tuples

tax = ('Homo', 'sapiens', 9606) # contstruct tuples
print(tax)

print(tax[0]) # calls the character in the 0 position
print(tax[::-1]) # lists the words backwards

# enumerate
nts = 'ACGT'
for i in range(len(nts)): # gives you index and value
	print(i, nts[i])
	
for i, nt in enumerate(nts): # a tidy alternative
	print(i, nt)
	
# zip()
names = ('adenine', 'cytosine', 'guanine', 'thymine')

for i in range(len(names)):
	print(nts[i], names[i])

for nt, name in zip(nts, names): # tidy version
	print(nt, name)

for i, (nt, name) in enumerate(zip(nts, names)): # gives you index, letter in that index, and name
	print(i, nt, name)

# lists
nts = ['A', 'T', 'C']
print(nts)
nts[2] = 'G'
print(nts)

nts.append('C') # adds a C to the end of the string list
print(nts)

last = nts.pop() # remove elements from the end of a list
print(last)

nts.sort() # sorts the elements (however must be the same type)
print(nts)
nts.sort(reverse=True) # sorts in reverse order
print(nts)

number = [22, 3, 50, 100]
number.sort()
print(number)
number.sort(reverse=True)
print(number)

nucleotides = nts # saving an existing list to a new variable
nucleotides.append('C')
nucleotides.sort()
print(nts, nucleotides) # modifcations occur in both because both variable names correspond to the same data

# list()
items = list() # create an empty list/container
print(items)

items.append('eggs') # add the word eggs to the container/list
print(items)

stuff = [] # can also create empty list with empty square brackets
stuff.append(3)
print(stuff)

alph = 'ACDEFGHIKLMPQRSVW'
print(alph)
aas = list(alph) # turns the string into a list of individual letters
print(aas)


# split()
# splits strings into lists of strings
text = 'good day	to you'
words = text.split() #splits strings into lists of strings
print(words)

line = '1.41, 2.72, 3.14'
print(line.split(',')) # splits string into list of strings separated by a comma

s = '-'.join(aas) # joins strings with a -
print(s)
s = '.'.join(aas)
print(s)

# searching 
# to search for items in a container you can use in, find(), and index()
if 'A' in alph: print('yay')
if 'a' in alph: print('no')

print('index G?', alph.index('G'))
'''print('index Z?', alph.index('Z')) # functions throws an error substring not found'''

# only useful for strings (not tuples or lists)
print('find G?', alph.find('G')) # returns the index of the frist element it finds
print('find Z?', alph.find('Z')) # returns a -1 if it cant be found

# searching in a list or tuple:
thing = ['cat', 'dog', 'bird', 'cow']
if 'bird' in thing: idx = thing.index('bird')
print(idx) # found on the second position














