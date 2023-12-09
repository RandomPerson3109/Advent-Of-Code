from time import time
from math import lcm
startTime = time()
inputF = open("input.txt","r")

inputList = inputF.read().split("\n\n")
inputList[1] = [i.split(" = ") for i in inputList[1].split("\n")]
string = [0 if i == "L" else 1 for i in inputList[0]]
graph = {}
startList = []
for i in inputList[1]:
	graph[i[0]] = i[1][1:-1].split(", ")
	if i[0][-1] == "A":
		startList.append(i[0])
lcmList = []
for i in startList:
	current = i
	count = 0
	while current[-1] != "Z":
		first = False
		current = graph[current][string[count%len(string)]]
		count += 1
	lcmList.append(count)
lcmN = 1
for i in lcmList:
	lcmN = lcm(lcmN, i)
print(lcmN)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
