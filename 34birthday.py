# 34birthday.py by Itzel Gonzalez

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
shared = 0


for i in range(trials):
	calendar = []	
	for day in range(days):
		calendar.append(0)	
	
	for people in range(people):
		birthday = random.randint(0, days-1)
		calendar[birthday] += 1
	
	collision = False
	for day in range(len(calendar)):
		if calendar[day] > 1: collision = True
		
	if collision: shared += 1

print(shared/trials)
		 
		
		
	

