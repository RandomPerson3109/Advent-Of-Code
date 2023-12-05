from time import time
startTime = time()
inputF = open("input.txt","r")

fullList = inputF.read().split("\n\n")
seedList = [int(i) for i in fullList[0].strip().split()[1:]]
fullList = [i.split("\n")[1:] for i in fullList[1:]]
for i in range(len(fullList)):
	for j in range(len(fullList[i])):
		fullList[i][j] = [int(k) for k in fullList[i][j].split()]

min = float("inf")
for i in seedList:
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
