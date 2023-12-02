from time import time
startTime = time()
inputF = open("input.txt","r")

digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
inputList = [i.split("\n")[0] for i in inputF.readlines()]
sum = 0
for i in inputList:
    val = 0
    condition = False
    while 1:
        for j in range(len(digit)):
            if digit[j] in i[0:val]:
                firstDigit = j%9+1
                condition = True
                break
        if condition:
            break
        val+=1
    val = len(i)-1
    condition = False
    while 1:
        for j in range(len(digit)):
            if digit[j] in i[val:len(i)]:
                secondDigit = j % 9 + 1
                condition = True
                break
        if condition:
            break
        val-=1
    sum += firstDigit*10+secondDigit
print(sum)

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))