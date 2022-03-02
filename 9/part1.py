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
tempMap = copy.deepcopy(inputs)

def findLowestPoints(inputMap):
    for input in inputMap:
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
        for j in range(len(inputMap)):
            if j != 0 and j != (len(inputMap) - 1):
                if inputMap[j][i] < inputMap[j-1][i] and inputMap[j][i] < inputMap[j+1][i]:
                    inputMap[j][i] += "y"
            if j == 0:
                if inputMap[j][i] < inputMap[j+1][i]:
                    inputMap[j][i] += "y"
            if j == (len(inputMap) - 1):
                if inputMap[j][i] < inputMap[j-1][i]:
                    inputMap[j][i] += "y"
    
    sum = 0
    for input in inputMap:
        for i in range(len(input)):
            if "xy" in input[i]:
                sum += int(input[i][:1]) + 1

    return sum

sum = findLowestPoints(tempMap)
print(sum)
