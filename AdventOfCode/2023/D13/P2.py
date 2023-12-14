from time import time
startTime = time()
inputF = open("input.txt","r")

def findVertical(l):
	for line in range(1, len(l[0])):
		foundMatch = True
		line1 = line-1
		line2 = line
		errors = 0
		while line2 < len(l[0]) and line1 >= 0:
			l1 = set(enumerate([l[i][line1] for i in range(len(l))]))
			l2 = set(enumerate([l[i][line2] for i in range(len(l))]))
			errors += len(l1.difference(l2))
			line1 -= 1
			line2 += 1
		if errors == 1:
			return line
	return 0
def findHorizontal(l):
	for line in range(1, len(l)):
		foundMatch = True
		line1 = line-1
		line2 = line
		errors = 0
		while line2 < len(l) and line1 >= 0:
			l1 = set(enumerate(l[line1]))
			l2 = set(enumerate(l[line2]))
			errors += len(l1.difference(l2))
			line1 -= 1
			line2 += 1
		if errors == 1:
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
