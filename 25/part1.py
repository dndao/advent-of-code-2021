import sys
import copy
from types import TracebackType

def getMap(file):
    with open(file) as f:
        seaCCBlines = f.read().splitlines()

    seaCCBmap = []
    for row in seaCCBlines:
        seaCCBmap.append([cCB for cCB in row])
    
    return(seaCCBmap)

seaCCBmap = getMap(sys.argv[1])

def printMap():
    for row in seaCCBmap:
        for seaCCB in row:
            print(seaCCB, end="")
        print()
    print("--------------")

printMap()

lastSeaCCBMap = copy.deepcopy(seaCCBmap)
stopMoving = False

def moveForward():
    global stopMoving

    # East herd moves first
    for row in seaCCBmap:
        for i in range(len(row)):
            if i < len(row) - 1:
                if (row[i] == ">" and row[i+1] == "."):
                    row[i] = "+"
                    row[i+1] = ">+"
            if i == len(row) - 1:
                if (row[i] == ">" and row[0] == "."):
                    row[i] = "+"
                    row[0] = ">+"
    
    for i in range(len(seaCCBmap)):
        for j in range(len(seaCCBmap[0])):
            if seaCCBmap[i][j] == ">+":
                seaCCBmap[i][j] = ">"
            if seaCCBmap[i][j] == "+":
                seaCCBmap[i][j] = "."

    # then South herd moves
    for i in range(len(seaCCBmap)):
        for j in range(len(seaCCBmap[0])):
            if i < len(seaCCBmap) - 1:
                if (seaCCBmap[i][j] == "v" and seaCCBmap[i+1][j] == "."):
                    seaCCBmap[i][j] = "+"
                    seaCCBmap[i+1][j] = "v+"
            if i == len(seaCCBmap) - 1:
                if (seaCCBmap[i][j] == "v" and seaCCBmap[0][j] == "."):
                    seaCCBmap[i][j] = "+"
                    seaCCBmap[0][j] = "v+"
    
    for i in range(len(seaCCBmap)):
        for j in range(len(seaCCBmap[0])):
            if seaCCBmap[i][j] == "v+":
                seaCCBmap[i][j] = "v"
            if seaCCBmap[i][j] == "+":
                seaCCBmap[i][j] = "."

step = 0
while(True):
    moveForward()
    if lastSeaCCBMap == seaCCBmap:
        break
    lastSeaCCBMap = copy.deepcopy(seaCCBmap)
    step += 1

print(step+1)