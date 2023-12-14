from time import time
startTime = time()
inputF = open("input.txt","r")

inputList = inputF.read().split("\n")
totalLoad = 0
for i in range(len(inputList[0])):
    load = len(inputList)
    for ji, j in enumerate([inputList[k][i] for k in range(len(inputList))]):
        if j == "O":
            totalLoad += load
            load -= 1
        elif j == "#":
            load = len(inputList) - ji - 1
print(totalLoad)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
