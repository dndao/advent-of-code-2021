import copy

def getInput(file):
    with open(file) as f:
        data = f.read().splitlines()

    data.remove("")

    foldInstructions = []
    positions = []

    for line in data:
        if "fold" in line:
            instruction = line[11:]
            instruction = (instruction.split("=")[0],instruction.split("=")[1])
            foldInstructions.append(instruction)
        else:
            position = (line.split(",")[0],line.split(",")[1])
            positions.append(position)

    return positions, foldInstructions

positions, foldInstructions = getInput("input.txt")

print(positions)
print(len(positions))
print(foldInstructions)

def findSize(positions):
    maxR = 0
    maxC = 0
    for duplets in positions:
        if int(duplets[0]) > maxC:
            maxC = int(duplets[0])
        if int(duplets[1]) > maxR:
            maxR = int(duplets[1])
    
    return maxR, maxC


def fillArray(positions):
    row, col = findSize(positions)
    arr = []
    for i in range(row+1):
        tempRow = []
        for j in range(col+1):
            tempRow.append(".")
        arr.append(tempRow)

    for duplets in positions:
        arr[int(duplets[1])][int(duplets[0])] = "#"
    
    return arr

def draw(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end="")
        print()
    print("---------------")

def foldUp(value, arr):
    tempArr = copy.deepcopy(arr)
    if len(tempArr) - value - 1 > value - 0:
        foldrange = value - 0
        for i in range(foldrange+1):
            for col in range(len(tempArr[0])):
                if tempArr[value+i][col] == "#":
                    tempArr[value-i][col] = tempArr[foldrange+i][col]
    elif len(tempArr) - value - 1 < value - 0:
        foldrange = len(tempArr) - value - 1
        for i in range(foldrange+1):
            for col in range(len(tempArr[0])):
                if tempArr[value+i][col] == "#":
                    tempArr[value-i][col] = tempArr[foldrange+i][col]
    else:
        foldrange = len(tempArr) - value - 1
        for i in range(foldrange+1):
            for col in range(len(tempArr[0])):
                if tempArr[value+i][col] == "#":
                    tempArr[value-i][col] = tempArr[foldrange+i][col]
    
    tempArr = tempArr[:value]

    return(tempArr)

def foldLeft(value, arr):
    tempArr = copy.deepcopy(arr)
    if len(tempArr[0]) - value - 1 > value - 0:
        foldrange = value - 0
        for row in range(len(tempArr)):
            for j in range(foldrange+1):
                if tempArr[row][value+j] == "#":
                    tempArr[row][value-j] = tempArr[row][value+j]
    elif len(tempArr[0]) - value - 1 < value - 0:
        foldrange = len(tempArr[0]) - value - 1
        for row in range(len(tempArr)):
            for j in range(foldrange+1):
                if tempArr[row][value+j] == "#":
                    tempArr[row][value-j] = tempArr[row][value+j]
    else:
        foldrange = len(tempArr[0]) - value - 1
        for row in range(len(tempArr)):
            for j in range(foldrange+1):
                if tempArr[row][value+j] == "#":
                    tempArr[row][value-j] = tempArr[row][value+j]

    newArr = []
    for row in tempArr:
        newArr.append(row[:value])

    return(newArr)

def countDot(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "#":
                count += 1
    
    return(count)

def runInstructions(positions, foldInstructions):
    arr = fillArray(positions)
    draw(arr)

    for instruction in foldInstructions:
        if instruction[0] == "x":
            arr = foldLeft(int(instruction[1]), arr)
            draw(arr)
        else:
            arr = foldUp(int(instruction[1]), arr)
            draw(arr)
    
    return(arr)

arr = runInstructions(positions, foldInstructions)
print(countDot(arr))