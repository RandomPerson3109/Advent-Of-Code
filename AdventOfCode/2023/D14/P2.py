from time import time
startTime = time()
inputF = open("input.txt","r")



inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))