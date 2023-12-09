from time import time
startTime = time()
inputF = open("input.txt","r")

inputList = inputF.read().split("\n\n")
inputList[1] = [i.split(" = ") for i in inputList[1].split("\n")]
string = [0 if i == "L" else 1 for i in inputList[0]]
graph = {}
for i in inputList[1]:
	graph[i[0]] = i[1][1:-1].split(", ")

current = "AAA"
count = 0
while current != "ZZZ":
	current = graph[current][string[count%len(string)]]
	count += 1
print(count)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
