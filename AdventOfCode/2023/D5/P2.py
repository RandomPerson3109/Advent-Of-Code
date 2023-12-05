from time import time
startTime = time()
inputF = open("input.txt","r")

def change(l, n):
	value = n
	for j in l:
		if value < j[0] or value >= j[0] + j[2]:
			continue
		else:
			value += j[1]-j[0]
			break
	return value

def findTurningPoints():
	turningPoints = set()
	for i in reversed(fullList):
		newTurningPoints = set()
		for j in i:
			turningPoints.add(j[1])
			turningPoints.add(j[1]+j[2])
		for j in turningPoints:
			newTurningPoints.add(change(i, j))
		turningPoints = newTurningPoints.copy()
	return turningPoints


fullList = inputF.read().split("\n\n")
seedList = [int(i) for i in fullList[0].strip().split()[1:]]
newSeedList = []
parity = 0
for i in seedList:
	parity = (parity+1)%2
	if parity:
		newSeedList.append([i])
	else:
		newSeedList[-1].append(i)
fullList = [i.split("\n")[1:] for i in fullList[1:]]
for i in range(len(fullList)):
	for j in range(len(fullList[i])):
		fullList[i][j] = [int(k) for k in fullList[i][j].split()]

turningPoints = list(findTurningPoints())

min = float("inf")
for i in turningPoints:
	okay = False
	for j in newSeedList:
		if i >= j[0] and i < j[0]+j[1]:
			okay = True
			break
	if not okay:
		continue
	value = i
	for j in fullList:
		counter = 0
		while value < j[counter][1] or value >= j[counter][1] + j[counter][2]:
			counter += 1
			if counter == len(j)-1:
				break
		if value < j[counter][1] or value >= j[counter][1] + j[counter][2]:
			continue
		else:
			value += j[counter][0]-j[counter][1]
			continue
	if value < min:
		min = value
print(min)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
