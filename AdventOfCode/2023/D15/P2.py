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
lens = [[] for _ in range(256)]
box = [[] for _ in range(256)]
for i in inputList:
    if i[-1] == "-": #remove the object
        hash = HASH(i[:-1])
        try:
            box[hash].index(i[:-1])
        except:
            continue
        else:
            value = box[hash].index(i[:-1])
            box[hash].pop(value)
            lens[hash].pop(value)
    else: #add the object
        fullI = i.split("=")
        hash = HASH(fullI[0])
        try:
            box[hash].index(fullI[0])
        except:
            box[hash].append(fullI[0])
            lens[hash].append(int(fullI[1]))
        else:
            value = box[hash].index(fullI[0])
            box[hash][value] = fullI[0]
            lens[hash][value] = int(fullI[1])
sum = 0
for i in range(len(lens)):
    for j in range(len(lens[i])):
        sum += lens[i][j]*(j+1)*(i+1)
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
