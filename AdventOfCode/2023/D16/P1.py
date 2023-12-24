from time import time
startTime = time()
inputF = open("input.txt","r")

def moveInDir(beam):
    x, y, dir = beam
    if dir == 0:
        y += 1
    elif dir == 1:
        x += 1
    elif dir == 2:
        y -= 1
    else:
        x -= 1
    return [x, y, dir]
def isSafeToAdd(beam):
    return beam[0] >= 0 and beam[0] < len(map) and beam[1] >= 0 and beam[1] < len(map[0])
def move(beam):
    x, y, dir = beam
    beams = set()
    if map[x][y] == "/":
        if dir == 0:
            dir = 3
        elif dir == 1:
            dir = 2
        elif dir == 2:
            dir = 1
        else:
            dir = 0
        toAdd = moveInDir([x, y, dir])
        if isSafeToAdd(toAdd):
            beams.add(tuple(toAdd))
    elif map[x][y] == "\\":
        if dir == 0:
            dir = 1
        elif dir == 1:
            dir = 0
        elif dir == 2:
            dir = 3
        else:
            dir = 2
        toAdd = moveInDir([x, y, dir])
        if isSafeToAdd(toAdd):
            beams.add(tuple(toAdd))
    elif map[x][y] == "|" and dir % 2 == 0: #If beam comes horizontally it splits the beam vertically
        toAdd = moveInDir([x, y, 1])
        if isSafeToAdd(toAdd):
            beams.add(tuple(toAdd))
        toAdd = moveInDir([x, y, 3])
        if isSafeToAdd(toAdd):
            beams.add(tuple(toAdd))
    elif map[x][y] == "-" and dir % 2 == 1: #If beam comes vertically it splits the beam horizontally
        toAdd = moveInDir([x, y, 0])
        if isSafeToAdd(toAdd):
            beams.add(tuple(toAdd))
        toAdd = moveInDir([x, y, 2])
        if isSafeToAdd(toAdd):
            beams.add(tuple(toAdd))
    else:
        toAdd = moveInDir([x, y, dir])
        if isSafeToAdd(toAdd):
            beams.add(tuple(toAdd))
    return beams

map = inputF.read().split("\n")
beams = {tuple([0, 0, 0])}
energized = set()
happened = set()
while len(beams) > 0:
    beam = list(beams.pop())
    happened.add(tuple(beam))
    energized.add(tuple(beam[:2]))
    beams.update(move(beam))
    beams.difference_update(happened)
print(len(energized))

inputF.close()
endTime = time()
msTaken = round((endTime-startTime)*1000, 3)
print("{}ms taken".format(msTaken))
