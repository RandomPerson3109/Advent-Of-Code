from time import time
startTime = time()
inputF = open("input.txt","r")

inputList = [i.strip().split(": ")[1] for i in inputF.readlines()]
winningNums = [[int(j.strip()) for j in i.split(" | ")[0].split()] for i in inputList]
haveNums = [[int(j.strip()) for j in i.split(" | ")[1].split()] for i in inputList]
sum = 0
for i, j in enumerate([_ for _ in range(len(winningNums))]):
    matches = -1
    for k in haveNums[i]:
        if k in winningNums[j]:
            matches += 1
    if matches >= 0:
        sum += 2**matches
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
