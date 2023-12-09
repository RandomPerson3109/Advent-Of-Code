from time import time
startTime = time()
inputF = open("input.txt","r")

def getNextNum(l):
    lastNums = [l[-1]]
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
        lastNums.append(l[-1])
    return sum(lastNums)

inputList = [[int(j) for j in i.split()] for i in inputF.readlines()]
sumList = []
for i in inputList:
    sumList.append(getNextNum(i))
print(sum(sumList))

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
