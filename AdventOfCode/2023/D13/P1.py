from time import time
startTime = time()
inputF = open("input.txt","r")

def findVertical(l):
	line = 1
	while line < len(l[0]):
		foundMatch = True
		line1 = line-1
		line2 = line
		while line2 < len(l[0]) and line1 >= 0:
			if [l[i][line1] for i in range(len(l))] != [l[i][line2] for i in range(len(l))]:
				line += 1
				foundMatch = False
				break
			line1 -= 1
			line2 += 1
		if foundMatch:
			return line
	return 0
def findHorizontal(l):
	line = 1
	while line < len(l):
		foundMatch = True
		line1 = line-1
		line2 = line
		while line2 < len(l) and line1 >= 0:
			if l[line1] != l[line2]:
				line += 1
				foundMatch = False
				break
			line1 -= 1
			line2 += 1
		if foundMatch:
			return line*100
	return 0

inputList = [i.split("\n") for i in inputF.read().split("\n\n")]
sum = 0
for i in inputList:
	sum += findVertical(i) + findHorizontal(i)
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
