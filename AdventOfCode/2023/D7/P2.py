from time import time
startTime = time()
inputF = open("input.txt","r")

def getHierarchy(l):
	instances = [set() for _ in range(5)]
	jokers = 0
	for i in l:
		if i == 1:
			jokers += 1
			continue
		done = False
		for j in range(4):
			if i in instances[j]:
				instances[j+1].add(i)
				instances[j].remove(i)
				done = True
				break
		if not done:
			instances[0].add(i)
	if len(instances[4]) != 0:
		return 6
	elif len(instances[3]) != 0:
		return 5 + jokers
	elif len(instances[2]) != 0:
		if len(instances[1]) != 0:
			return 4
		else:
			return 3 if jokers == 0 else 4 + jokers
	elif len(instances[1]) == 2:
		return 2 if jokers == 0 else 4
	elif len(instances[1]) == 1:
		return 1 if jokers == 0 else 3 if jokers == 1 else 3 + jokers
	else:
		return 0 if jokers == 0 else 1 if jokers == 1 else 3 if jokers == 2 else 2 + jokers if jokers == 3 or jokers == 4 else 6

inputList = [i.strip().split() for i in inputF.readlines()]
for i in inputList:
	i[0] = [10 if i == 'T' else 1 if i == 'J' else 11 if i == 'Q' else 12 if i == 'K' else 13 if i == 'A' else int(i) for i in list(i[0])]
	i[1] = int(i[1])
hierarchy = [[] for _ in range(7)]
for i in inputList:
	hierarchy[getHierarchy(i[0])].append(i)
hierarchy = list(map(sorted, hierarchy))
sum = 0
counter = 0
for i in hierarchy:
	for j in i:
		counter += 1
		sum += counter*j[1]
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
