from time import time
startTime = time()
inputF = open("input.txt","r")

fullList = inputF.readlines()
seedsList = [int(i) for i in fullList[0].strip().split()[1:]]
fullList = fullList[2:]
print(fullList)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
