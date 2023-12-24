from time import time
startTime = time()
inputF = open("input.txt","r")

def findMax(l):
    curPos = [0, 0]
    allPos = []
    value = 0
    for i in l:
        allPos.append(curPos[:])
        if i[0] == "R":
            curPos[1] += i[1]
        elif i[0] == "L":
            curPos[1] -= i[1]
        elif i[0] == "U":
            curPos[0] += i[1]
        else:
            curPos[0] -= i[1]
    allPos.append([0, 0])
    for i in range(len(allPos)-1):
        value += allPos[i][0]*allPos[i+1][1] - allPos[i][1]*allPos[i+1][0]
    return int(abs(value)/2)

inputList = [[int(i.split()[-1][-2]), i.split()[-1][2:-2]] for i in inputF.read().split("\n")]
for i in inputList:
    i[0] = "R" if i[0] == 0 else "D" if i[0] == 1 else "L" if i[0] == 2 else "U"
    i[1] = int(i[1], 16)
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
print(findMax(inputList) + sum([i[1] if i[0] in ["L", "D"] else 0 for i in inputList]) + 1)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
