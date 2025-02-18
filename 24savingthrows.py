# 24savingthrow.py by Itzel Gonzalez
import random

trials = 5
dc = 5
success = 0


def advantage():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 > roll2: return roll1
	return roll2
	
def disadvantage(): 
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 < roll2: return roll1
	return roll2

for i in range(trials): # normally
	roll = random.randint(1, 20)
	if roll >= dc: success += 1
	print(i, roll) 
print(success/trials)


for dc in range(5, 16, 5): # starts at 5, ends at 15, step of 5
	success = 0
	for i in range(trials):
		roll = disadvantage()
		if roll >= dc: success += 1
	print(dc, success/trials)

for dc in range(5, 16, 5): 
	nor = 0
	adv = 0
	dis = 0
	for i in range(trials):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 >= dc: nor += 1
		if r1 >= dc and r2 >= dc: dis += 1
		if r1 >= dc or r2 >= dc: adv += 1
	print(dc, nor/trials, dis/trials, adv/trials)