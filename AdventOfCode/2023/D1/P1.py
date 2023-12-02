from time import time
startTime = time()
inputF = open("input.txt","r")

inputList = [i.split("\n")[0] for i in inputF.readlines()]
sum = 0
for i in inputList:
    digits = []
    for letter in i:
        if letter.isnumeric():
            digits.append(int(letter))
    sum += digits[0]*10+digits[-1]
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))