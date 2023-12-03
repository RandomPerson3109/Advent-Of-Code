from time import time
startTime = time()
inputF = open("input.txt","r")

def searchNum(x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if numList[i][j].isnumeric():
                numIncluded.append("{} {}".format(i, j))

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
notSymbol = "1 2 3 4 5 6 7 8 9 0 .".split()
numList = [i.strip() for i in inputF.readlines()]
numIncluded = []
for i in range(len(numList)):
    for j in range(len(numList[i])):
        if numList[i][j] not in notSymbol:
            searchNum(i, j)
while len(numIncluded) > 0:
    if len(numIncluded) != 1:
        if int(numIncluded[-1].split()[0]) == int(numIncluded[-2].split()[0]) and int(numIncluded[-1].split()[1])-1 == int(numIncluded[-2].split()[1]):
            numIncluded.pop(-1)
            continue
    sum += findValue(int(numIncluded[-1].split()[0]), int(numIncluded[-1].split()[1]))
    numIncluded.pop(-1)

print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
