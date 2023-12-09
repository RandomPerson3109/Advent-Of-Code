from time import time
startTime = time()
inputF = open("input.txt","r")

def getPrevNum(l):
    firstNums = [l[0]]
    while 1:
        for i in l:
            if i == 0:
                allZero = True
            else:
                allZero = False
                break
        if allZero:
            break
        for i in range(len(l)-1):
            l[i] = l[i+1]-l[i]
        l.pop(-1)
        firstNums.append(l[0])
    returnValue = 0
    for i in reversed(firstNums[:-1]):
        returnValue = i-returnValue
    return returnValue

inputList = [[int(j) for j in i.split()] for i in inputF.readlines()]
sumList = []
for i in inputList:
    sumList.append(getPrevNum(i))
print(sum(sumList))

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
