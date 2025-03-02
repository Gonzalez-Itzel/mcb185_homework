# 33birthday.py by Itzel Gonzalez
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
shared = 0

for t in range(trials):
	classroom = []
	for student in range(people):
		birthday = random.randint(0, days)
		if birthday in classroom:
			shared += 1
			break
		classroom.append(birthday)
print(shared/trials)








	
	
	














