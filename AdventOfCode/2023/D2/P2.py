from time import time
startTime = time()
inputF = open("input.txt","r")

from time import time
startTime = time()
inputF = open("input.txt","r")

gameList = [[j.split() for j in i.split(": ")[1].strip().replace(';', ',').split(", ")] for i in inputF.readlines()]
changeList = {"red" : 0, "green" : 1, "blue": 2}
sum = 0
for i in gameList:
    maxList = [0, 0, 0]
    for j in i:
        if int(j[0]) > maxList[changeList[j[1]]]:
            maxList[changeList[j[1]]] = int(j[0])
    sum += maxList[0]*maxList[1]*maxList[2]
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
