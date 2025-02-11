# 25deathsaves.py by Itzel Gonzalez

'''
20: revive
10 - 19: 1 success
2 - 9: 1 failure
1:  2 failures

if you accumulate 3 successes = stable
3 failures = death
'''
import random

trial = 10000
die = 0
stable = 0
revive = 0 

# make a for loop for every trial
for i in range(trial):
	failure = 0
	success = 0
	
	for i in range(5):  
		r = random.randint(1, 20)
		if r == 1: failure += 2 
		elif r < 10: failure += 1
		elif r < 20: success += 1 
		else: 
			revive += 1
			break
		if success == 3:
			stable += 1
			break
		if failure >= 3:
			die += 1
			break
print(die/trial, stable/trial, revive/trial) # the probability one dies, stabilizes, or revives
		
		
	