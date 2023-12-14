from time import time

startTime = time()
inputF = open("input.txt", "r")


def searchWASD(x, y):
	connection = [["-", "7", "J"], ["|", "L", "J"], ["-", "F", "L"], ["|", "F", "7"]]
	conversion = {0: 2, 2: 0, 1: 3, 3: 1}
	toSearch = [[x, y + 1], [x + 1, y], [x, y - 1], [x - 1, y]]
	for j, i in enumerate(toSearch):
		if i[0] < 0 or i[0] >= len(inputList) or i[1] < 0 or i[1] >= len(inputList[i[0]]) or tuple(i) in allPos:
			continue
		if inputList[i[0]][i[1]] in connection[j] and inputList[x][y] in connection[conversion[j]]:
			return i

def startConnected():
	connection = [["|", "F", "7"], ["|", "L", "J"], ["-", "F", "L"], ["-", "7", "J"]]
	toSearch = [[startPos[0]-1, startPos[1]], [startPos[0]+1, startPos[1]], [startPos[0], startPos[1]-1], [startPos[0], startPos[1]+1]]
	connections = []
	for j, i in enumerate(toSearch):
		if i[0] < 0 or i[0] >= len(inputList) or i[1] < 0 or i[1] >= len(inputList[i[0]]):
			continue
		if inputList[i[0]][i[1]] in connection[j]:
			connections.append(i)
	return connections

inputList = [list(i) for i in inputF.read().split("\n")]
startPos = []
allPos = set()
foundStartPos = False
for iI, i in enumerate(inputList):
	for jI, j in enumerate(i):
		if j == "S":
			startPos = [iI, jI]
			foundStartPos = True
			break
	if foundStartPos:
		break

startConnection = startConnected()
posToSearch = startConnection[0]
if [startPos[0] + 1, startPos[1]] in startConnection:  # Down
	if [startPos[0], startPos[1] + 1] in startConnection:  # Right
		inputList[startPos[0]][startPos[1]] = "F"
	elif [startPos[0] - 1, startPos[1]] in startConnection:  # Up
		inputList[startPos[0]][startPos[1]] = "|"
	else:  # Left
		inputList[startPos[0]][startPos[1]] = "7"
elif [startPos[0] - 1, startPos[1]] in startConnection:  # Up
	if [startPos[0], startPos[1] + 1] in startConnection:  # Right
		inputList[startPos[0]][startPos[1]] = "L"
	else: # Left
		inputList[startPos[0]][startPos[1]] = "J"
else:  # Left-Right
	inputList[startPos[0]][startPos[1]] = "-"

while 1:
	allPos.add(tuple(posToSearch))
	posToSearch = searchWASD(posToSearch[0], posToSearch[1])
	if posToSearch == None:
		break
area = 0
for i in range(len(inputList)):
	walls = 0
	firstConnection = None
	for j in range(len(inputList[i])):
		if tuple([i, j]) in allPos:
			if inputList[i][j] in ["L", "F"]:
				if inputList[i][j] == "L":
					firstConnection = 1
				else:
					firstConnection = 0
			elif inputList[i][j] in ["J", "7"]:
				if inputList[i][j] == "J":
					if firstConnection == 0:
						walls += 1
				else:
					if firstConnection == 1:
						walls += 1
				firstConnection = None
			elif inputList[i][j] != "-":
				walls += 1
		elif walls % 2 != 0:
			area += 1
print(area)

inputF.close()
endTime = time()
msTaken = round((endTime - startTime) * 1000, 3)
print("{}ms taken".format(msTaken))
