import gzip
import sys

count = {}

'''
# counting all of the features in a GFF
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp: # loops through each line in the file
		if line.startswith('#'): continue # if line starts with # then it continues 
		f = line.split() # splits the lines into columns
		feature = f[2] # extracts the second column
		if feature not in count: count[feature] = 0 # if the feature is not in the dictionary, must create key before we can start counting
		count[feature] += 1 # does the counting under the assumption that they key is in the table
for f, n in count.items(): print(f,n) # reports the counts of each feature
'''

# counting nucletotides using dictionary
count = {} # initialize empty dictionary
for nt in seq:
	if nt not in count: count[nt] = 0 # initialize its count to 0
	count[nt] += 1 # increment by one to add to dictionary
	
for k in sorted(count): print(k, count[k]) # sorts key inside of python 