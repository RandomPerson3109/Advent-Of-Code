from time import time
startTime = time()
inputF = open("input.txt","r")

def searchNum(x, y):
    temp = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if numList[i][j].isnumeric():
                if len(temp) != 0 and ((j>=y and numList[i][j-1].isnumeric()) or (j<=y and numList[i][j+1].isnumeric())) and i in [int(k.split()[0]) for k in temp]:
                    continue
                temp.append("{} {}".format(i, j))
    if len(temp) == 2:
        numIncluded.append(temp)

def findValue(x, y):
    value = [numList[x][y]]
    start, end = y-1, y+1
    while start>=0 and numList[x][start].isnumeric():
        value.insert(0, numList[x][start])
        start -= 1
    while end<len(numList[0]) and numList[x][end].isnumeric():
        value.append(numList[x][end])
        end += 1
    return int(''.join(value))

sum = 0
numList = [i.strip() for i in inputF.readlines()]
numIncluded = []
for i in range(len(numList)):
    for j in range(len(numList[i])):
        if numList[i][j] == "*":
            searchNum(i, j)
while len(numIncluded) > 0:
    sum += findValue(int(numIncluded[-1][0].split()[0]), int(numIncluded[-1][0].split()[1])) * findValue(int(numIncluded[-1][1].split()[0]), int(numIncluded[-1][1].split()[1]))
    numIncluded.pop(-1)
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
