from time import time
from math import sqrt, floor, ceil
startTime = time()
inputF = open("input.txt","r")

inputList = [int(''.join([j for j in i.strip().split()[1:]])) for i in inputF.readlines()]
print(floor((inputList[0]+sqrt(inputList[0]**2-inputList[1]*4))/2) - ceil((inputList[0]-sqrt(inputList[0]**2-inputList[1]*4))/2) + 1)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
