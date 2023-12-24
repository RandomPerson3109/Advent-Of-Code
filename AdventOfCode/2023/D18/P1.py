from time import time
startTime = time()
inputF = open("input.txt","r")

def setChar(x, y, dir):
    toSearch = {(x, y+1, 0), (x+1, y, 1), (x, y-1, 2), (x-1, y, 3)}
    dirs = set()
    dirs.add(0 if dir == "R" else 1 if dir == "D" else 2 if dir == "L" else 3)
    for i in toSearch:
        if i[0] < 0 or i[0] >= len(map) or i[1] < 0 or i[1] >= len(map[0]):
            continue
        if map[i[0]][i[1]] == ("-" if i[2] % 2 == 0 else "|"):
            dirs.add(i[2])
            break
    if 0 in dirs and 1 in dirs:
        map[x][y] = "F"
    elif 1 in dirs and 2 in dirs:
        map[x][y] = "7"
    elif 2 in dirs and 3 in dirs:
        map[x][y] = "J"
    else:
        map[x][y] = "L"

inputList = [i.split()[:-1] for i in inputF.read().split("\n")]
maxH = maxW = minH = minW = curH = curW = 0
for i in inputList:
    i[1] = int(i[1])
    if i[0] == "R":
        curW += i[1]
        maxW = max(maxW, curW)
    elif i[0] == "L":
        curW -= i[1]
        minW = min(minW, curW)
    elif i[0] == "U":
        curH += i[1]
        maxH = max(maxH, curH)
    else:
        curH -= i[1]
        minH = min(minH, curH)
height = maxH - minH + 1
width = maxW - minW + 1
startPos = (maxH, abs(minW))
curPos = [startPos[0], startPos[1]]
map = [["." for i in range(width)] for j in range(height)]
map[startPos[0]][startPos[1]] = "S"
for i in inputList:
    if i[0] == "R":
        index = 1
        pos = 1
        char = "-"
        if map[curPos[0]][curPos[1]] != "S":
            setChar(curPos[0], curPos[1], "R")
    elif i[0] == "L":
        index = 1
        pos = -1
        char = "-"
        if map[curPos[0]][curPos[1]] != "S":
            setChar(curPos[0], curPos[1], "L")
    elif i[0] == "U":
        index = 0
        pos = -1
        char = "|"
        if map[curPos[0]][curPos[1]] != "S":
            setChar(curPos[0], curPos[1], "U")
    else:
        index = 0
        pos = 1
        char = "|"
        if map[curPos[0]][curPos[1]] != "S":
            setChar(curPos[0], curPos[1], "D")
    for j in range(i[1]):
        curPos[index] += pos
        map[curPos[0]][curPos[1]] = char
setChar(startPos[0], startPos[1], inputList[0][0])

area = 0
for i in map:
    walls = 0
    for j in i:
        if j in ["|", "F", "7"]:
            walls += 1
        elif j == ".":
            if walls % 2 != 0:
                area += 1
print(area + sum([i[1] for i in inputList]))

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
