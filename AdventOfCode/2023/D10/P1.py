from time import time
startTime = time()
inputF = open("input.txt","r")

def searchWASD(x, y, isS = False):
    connection = [["|", "F", "7"], ["|", "L", "J"], ["-", "F", "L"], ["-", "7", "J"]]
    conversion = {0: 1, 1: 0, 2: 3, 3: 2}
    toSearch = [[x-1, y, 0], [x+1, y, 1], [x, y-1, 2], [x, y+1, 3]]
    connections = []
    for i in toSearch:
        if i[0] < 0 or i[0] >= len(inputList) or i[1] < 0 or i[1] >= len(inputList[i[0]]):
            continue
        if inputList[i[0]][i[1]] in connection[i[2]] and (isS or inputList[x][y] in connection[conversion[i[2]]]):
            connections.append(i[0:2])
    return connections

inputList = [list(i) for i in inputF.read().split("\n")]
startPos = []
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
length = 0
while 1:
    newPos = []
    length += 1
    while len(posToSearch) > 0:
        i = posToSearch.pop(-1)
        newPos += searchWASD(i[0], i[1])
        inputList[i[0]][i[1]] = "."
    if len(newPos) == 0:
        break
    posToSearch = newPos
print(length)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
