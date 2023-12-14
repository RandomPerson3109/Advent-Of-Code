from time import time
startTime = time()
inputF = open("input.txt","r")

def moveUp(l):
    newL = [list(i) for i in l]
    for i in range(len(newL[0])):
        placeable = 0
        for ji, j in enumerate([newL[k][i] for k in range(len(newL))]):
            if j == "O":
                newL[ji][i] = "."
                newL[placeable][i] = "O"
                placeable += 1
            elif j == "#":
                placeable = ji + 1
    return ["".join(i) for i in newL]
def moveDown(l):
    newL = [list(i) for i in l]
    for i in range(len(newL[0])):
        placeable = len(newL)-1
        for ji, j in enumerate(reversed([newL[k][i] for k in range(len(newL))])):
            if j == "O":
                newL[len(newL)-ji-1][i] = "."
                newL[placeable][i] = "O"
                placeable -= 1
            elif j == "#":
                placeable = len(newL) - ji - 2
    return ["".join(i) for i in newL]

def moveLeft(l):
    newL = [list(i) for i in l]
    for i in range(len(newL)):
        placeable = 0
        for ji, j in enumerate(newL[i]):
            if j == "O":
                newL[i][ji] = "."
                newL[i][placeable] = "O"
                placeable += 1
            elif j == "#":
                placeable = ji + 1
    return ["".join(i) for i in newL]

def moveRight(l):
    newL = [list(i) for i in l]
    for i in range(len(newL)):
        placeable = len(newL[i])-1
        for ji, j in enumerate(reversed(newL[i])):
            if j == "O":
                newL[i][len(newL[i])-ji-1] = "."
                newL[i][placeable] = "O"
                placeable -= 1
            elif j == "#":
                placeable = len(newL[i]) - ji - 2
    return ["".join(i) for i in newL]

def cycle(l):
    return moveRight(moveDown(moveLeft(moveUp(l))))

inputList = inputF.read().split("\n")
totalLoads = []
while len(totalLoads) < 1000:
    totalLoad = 0
    for i in range(len(inputList), 0, -1):
        totalLoad += list(inputList[len(inputList)-i]).count("O")*i
    totalLoads.append(totalLoad)
    print(totalLoad)
    inputList = cycle(inputList)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
