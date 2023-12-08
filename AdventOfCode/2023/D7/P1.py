from time import time
startTime = time()
inputF = open("input.txt","r")

def getHierarchy(l):
	instances = [set() for _ in range(5)]
	for i in l:
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
		return 5
	elif len(instances[2]) != 0:
		if len(instances[1]) != 0:
			return 4
		else:
			return 3
	else:
		return len(instances[1])

inputList = [i.strip().split() for i in inputF.readlines()]
for i in inputList:
	i[0] = [10 if i == 'T' else 11 if i == 'J' else 12 if i == 'Q' else 13 if i == 'K' else 14 if i == 'A' else int(i) for i in list(i[0])]
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
