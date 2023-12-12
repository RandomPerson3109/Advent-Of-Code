from time import time
startTime = time()
inputF = open("input.txt","r")

inputList = [list(i) for i in inputF.read().split("\n")]
rowToAdd = set()
for i in range(len(inputList)):
    if inputList[i] == ["." for _ in inputList[i]]:
        rowToAdd.add(i)
columnToAdd = set()
for i in range(len(inputList[0])):
    if [inputList[j][i] for j in range(len(inputList))] == ["." for _ in inputList]:
        columnToAdd.add(i)
stars = set()
for i in range(len(inputList)):
    for j in range(len(inputList[i])):
        if inputList[i][j] == "#":
            stars.add(tuple([i, j]))
distance = 0
while len(stars) > 0:
    search = stars.pop()
    for i in stars:
        distance += abs(i[0]-search[0]) + abs(i[1]-search[1])
        for j in rowToAdd:
            if (i[0] < j < search[0]) or (i[0] > j > search[0]):
                distance += 1
        for j in columnToAdd:
            if (i[1] < j < search[1]) or (i[1] > j > search[1]):
                distance += 1
print(distance)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
