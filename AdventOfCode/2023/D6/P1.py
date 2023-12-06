from time import time
from math import sqrt, floor, ceil
startTime = time()
inputF = open("input.txt","r")

inputList = [[int(j) for j in i.strip().split()[1:]] for i in inputF.readlines()]
product = 1
for t, d in zip(inputList[0], inputList[1]):
    product *= floor((t+sqrt(t**2-d*4))/2) - ceil((t-sqrt(t**2-d*4))/2) + 1
print(product)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
