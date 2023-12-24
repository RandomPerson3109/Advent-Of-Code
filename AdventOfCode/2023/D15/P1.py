from time import time
startTime = time()
inputF = open("input.txt","r")

def HASH(s):
    hash = 0
    for i in s:
        hash += ord(i)
        hash *= 17
        hash %= 256
    return hash

inputList = inputF.read().split(",")
sum = 0
for i in inputList:
    sum += HASH(i)
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
