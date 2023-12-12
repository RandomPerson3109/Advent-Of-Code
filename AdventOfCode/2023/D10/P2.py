from time import time

startTime = time()
inputF = open("input.txt", "r")


def searchWASD(x, y, isS=False):
    connection = [["-", "7", "J"], ["|", "L", "J"], ["-", "F", "L"], ["|", "F", "7"]]
    conversion = {0: 2, 2: 0, 1: 3, 3: 1}
    toSearch = [[x, y + 1], [x + 1, y], [x, y - 1], [x - 1, y]]
    for j, i in enumerate(toSearch):
        if i[0] < 0 or i[0] >= len(inputList) or i[1] < 0 or i[1] >= len(inputList[i[0]]) or tuple(i) in allPos:
            continue
        if inputList[i[0]][i[1]] in connection[j] and (isS or inputList[x][y] in connection[conversion[j]]):
            return i


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

posToSearch = searchWASD(startPos[0], startPos[1], True)
if [startPos[0] + 1, startPos[1]] in posToSearch:  # Down
    if [startPos[0], startPos[1] + 1] in posToSearch:  # Right
        inputList[startPos[0]][startPos[1]] = "J"
    else:  # Left
        inputList[startPos[0]][startPos[1]] = "L"
else:  # Up
    if [startPos[0], startPos[1] + 1] in posToSearch:  # Right
        inputList[startPos[0]][startPos[1]] = "7"
    else:  # Left
        inputList[startPos[0]][startPos[1]] = "F"
print('\n'.join([''.join(i) for i in inputList]))

while 1:
    allPos.add(tuple(posToSearch))
    posToSearch = searchWASD(posToSearch[0], posToSearch[1])
    if posToSearch == None:
        break
print(allPos)
area = 0
for i in range(len(inputList)):
    walls = 0
    connected = False
    firstConnection = True
    for j in range(len(inputList[i])):
        if tuple([i, j]) in allPos:
            if inputList[i][j] in ["-", "L", "F"]:
                connected = True
                if firstConnection:
                    walls += 1
                    firstConnection = False
            else:
                walls += 1
                connected = False
                firstconnection = True
        elif walls % 2 != 0:
            area += 1
print(area)

inputF.close()
endTime = time()
msTaken = round((endTime - startTime) * 1000, 3)
print("{}ms taken".format(msTaken))
