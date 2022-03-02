import copy

def getInput(file):
    input = []
    with open(file) as f:
        data = f.read().splitlines()

    for line in data:
        temp = [char for char in line]
        input.append(temp)

    return input

inputs = getInput("input.txt")

def findLowestPoints(inputs):
    tempMap = copy.deepcopy(inputs)
    for input in tempMap:
        for i in range(len(input)):
            if i != 0 and i != (len(input) - 1):
                if input[i] < input[i-1] and input[i] < input[i+1]:
                    input[i] += "x"
            if i == len(input) - 1:
                if input[i] < input[i-1]:
                    input[i] += "x"
            if i == 0:
                if input[i] < input[i+1]:
                    input[i] += "x"
    
    for i in range(len(input)):
        for j in range(len(tempMap)):
            if j != 0 and j != (len(tempMap) - 1):
                if tempMap[j][i] < tempMap[j-1][i] and tempMap[j][i] < tempMap[j+1][i]:
                    tempMap[j][i] += "y"
            if j == 0:
                if tempMap[j][i] < tempMap[j+1][i]:
                    tempMap[j][i] += "y"
            if j == (len(tempMap) - 1):
                if tempMap[j][i] < tempMap[j-1][i]:
                    tempMap[j][i] += "y"
    
    lowestPoints = []
    for i in range(len(tempMap)):
        for j in range(len(tempMap[i])):
            if "xy" in tempMap[i][j]:
                lowestPoints.append((i,j))

    return lowestPoints

points = findLowestPoints(inputs)

def getNumber(string):
    arr = string.split()
    return arr[0]

def checkFourDirection(point, tempMap):
    current = tempMap[point[0]][point[1]]
    if point[0] != 0:
        up = (point[0]-1,point[1])
    else:
        up = None
    if point[0] != (len(tempMap) - 1):
        down = (point[0]+1,point[1])
    else:
        down = None    
    if point[1] != 0:
        left = (point[0],point[1]-1)
    else:
        left = None 
    if point[1] != (len(tempMap[0]) - 1):
        right = (point[0],point[1]+1)
    else:
        right = None

    if up is not None: 
        if getNumber(tempMap[up[0]][up[1]]) > getNumber(current) and tempMap[up[0]][up[1]] != "9" and "x" not in tempMap[up[0]][up[1]]:
            tempMap[up[0]][up[1]] += "x"
            tempMap = checkFourDirection(up, tempMap)
    if down is not None: 
        if tempMap[down[0]][down[1]] > current and tempMap[down[0]][down[1]] != "9" and "x" not in tempMap[down[0]][down[1]]:
            tempMap[down[0]][down[1]] += "x"
            tempMap = checkFourDirection(down, tempMap)
    if left is not None: 
        if tempMap[left[0]][left[1]] > current and tempMap[left[0]][left[1]] != "9" and "x" not in tempMap[left[0]][left[1]]:
            tempMap[left[0]][left[1]] += "x"
            tempMap = checkFourDirection(left, tempMap)
    if right is not None: 
        if tempMap[right[0]][right[1]] > current and tempMap[right[0]][right[1]] != "9" and "x" not in tempMap[right[0]][right[1]]:
            tempMap[right[0]][right[1]] += "x"
            tempMap = checkFourDirection(right, tempMap)
    return(tempMap)

def countBasin(point, tempMap):
    markedMap = checkFourDirection(point, tempMap)
    count = 1
    for i in range(len(markedMap)):
        for j in range(len(markedMap[0])):
            if "x" in markedMap[i][j]:
                count += 1
    
    return(count)


def findBasins(points, inputs):
    basins = []
    for point in points:
        tempMap = copy.deepcopy(inputs)
        count = countBasin(point, tempMap)
        basins.append(count)
    
    basins.sort()
    score = basins[len(basins)-1] * basins[len(basins)-2] * basins[len(basins)-3]
    return(score)

score = findBasins(points, inputs)
print(score)