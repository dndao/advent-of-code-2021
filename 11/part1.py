import copy

def getInput(file):
    input = []
    with open(file) as f:
        data = f.read().splitlines()

    for line in data:
        temp = [char for char in line]
        input.append(temp)

    return input

octopuses = getInput("testinput.txt")

def increaseOne(octopuses):
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            octopuses[i][j] = str(int(octopuses[i][j])+1)

def increaseAdjacent(i,j):
    if (i != 0):
        if ("x" not in octopuses[i-1][j]):
            octopuses[i-1][j] = str(int(octopuses[i-1][j])+1)
    if (i != (len(octopuses)-1)):
        if ("x" not in octopuses[i+1][j]):
            octopuses[i+1][j] = str(int(octopuses[i+1][j])+1)
    if (j != 0):
        if ("x" not in octopuses[i][j-1]):
            octopuses[i][j-1] = str(int(octopuses[i][j-1])+1)
        if (i != 0):
            if ("x" not in octopuses[i-1][j-1]):
                octopuses[i-1][j-1] = str(int(octopuses[i-1][j-1])+1)
        if (i != (len(octopuses)-1)):
            if ("x" not in octopuses[i+1][j-1]):
                octopuses[i+1][j-1] = str(int(octopuses[i+1][j-1])+1)
    if (j != (len(octopuses[0])-1)):
        if ("x" not in octopuses[i][j+1]):
            octopuses[i][j+1] = str(int(octopuses[i][j+1])+1)
        if (i != 0):
            if ("x" not in octopuses[i-1][j+1]):
                octopuses[i-1][j+1] = str(int(octopuses[i-1][j+1])+1)
        if (i != (len(octopuses)-1)):
            if ("x" not in octopuses[i+1][j+1]):
                octopuses[i+1][j+1] = str(int(octopuses[i+1][j+1])+1)
                
def removeMarks(octopus):
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            if "x" in octopuses[i][j]:
                octopuses[i][j] = "0"

def checkFlashes(count, octopuses):
    current = (0,0)
    flashed = True
    for i in range(len(octopuses)):
        for j in range(len(octopuses[0])):
            if "x" not in octopuses[i][j]:
                if int(octopuses[i][j]) > 9:
                    count += 1
                    octopuses[i][j] += "x"
                    current = (i,j)
                    increaseAdjacent(i,j)
                    flashed = False
    if(not flashed):
        checkFlashes(count, octopuses)
        
    return(count)

    
def stimulateSteps(steps, octopuses):
    totalCount = 0
    for step in range(steps):
        print("Step: ", step+1)
        # increase energy by 1
        increaseOne(octopuses)
        totalCount += checkFlashes(0, octopuses)
        removeMarks(octopuses)
        print(octopuses)

    return(totalCount)

flashedTimes = stimulateSteps(10, octopuses)
print(flashedTimes)