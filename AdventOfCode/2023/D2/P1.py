from time import time
startTime = time()
inputF = open("input.txt","r")

from time import time
startTime = time()
inputF = open("input.txt","r")

gameList = [[j.split() for j in i.split(": ")[1].strip().replace(';', ',').split(", ")] for i in inputF.readlines()]
changeList = {"red" : 0, "green" : 1, "blue": 2}
sum = 0
id = 0
for i in gameList:
    id += 1
    maxList = [0, 0, 0]
    for j in i:
        if int(j[0]) > maxList[changeList[j[1]]]:
            maxList[changeList[j[1]]] = int(j[0])
    if maxList[0] <= 12 and maxList[1] <= 13 and maxList[2] <= 14:
        sum += id
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
