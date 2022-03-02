import copy

def getInput(file):
    input = []
    with open(file) as f:
        data = f.read().splitlines()

    for line in data:
        temp = (line.split("-")[0],line.split("-")[1])
        input.append(temp)

    return input

inputs = getInput("testinput.txt")

def getOutput(file):
    output = []
    with open(file) as f:
        data = f.read().splitlines()

    for line in data:
        temp = [value for value in line.split(",")]
        output.append(temp)

    return output

outputs = getOutput("testoutput.txt")
inputs = getInput("testinput.txt")

def createDictionary(inputs):
    routeDict = {}
    for input in inputs:
        if input[0] in routeDict:
            routeDict[input[0]].append(input[1])
            if input[1].islower() and input[1] != "start" and input[1] != "end":
                routeDict[input[0]].append(input[1])
        else:
            routeDict[input[0]] = []
            routeDict[input[0]].append(input[1])
            if input[1].islower() and input[1] != "start" and input[1] != "end":
                routeDict[input[0]].append(input[1])
        if input[1] in routeDict:
            routeDict[input[1]].append(input[0])
            if input[0].islower() and input[0] != "start" and input[0] != "end":
                routeDict[input[1]].append(input[0])
        else:
            routeDict[input[1]] = []
            routeDict[input[1]].append(input[0])
            if input[0].islower() and input[0] != "start" and input[0] != "end":
                routeDict[input[1]].append(input[0])
    
    for key in routeDict.keys():
        if key != "start" or key != "end":
            if "start" in routeDict[key]:
                routeDict[key].remove("start")
    
    return(routeDict)

routeDict = createDictionary(inputs)
print(routeDict)

def findOptions(paths, path, option):
    for value in routeDict[option]:
        tempPath = copy.deepcopy(path)
        if (value not in tempPath) and ("end" not in tempPath):
            tempPath.append(value)
            findOptions(paths, tempPath, value)
            paths.append(tempPath)

def doesNotHaveTwoLowers(path):
    for value in path:
        if value.islower() and path.count(value) > 1:
            return False
    return True

def addEnd(paths):
    for path in paths:
        tempPath = copy.deepcopy(path)
        if tempPath[-1] != "end" and ("end" in routeDict[tempPath[-1]]):
            tempPath.append("end")
            if tempPath not in paths:
                paths.append(tempPath)

def addRoute(paths):
    for path in paths:
        if path[-1] != "end":
            for value in routeDict[path[-1]]:
                tempPath = copy.deepcopy(path)
                if value.islower() and doesNotHaveTwoLowers(tempPath):
                    tempPath.append(value)
                    if tempPath not in paths:
                        paths.append(tempPath)
                if value.isupper():
                    tempPath.append(value)
                    if tempPath not in paths:
                        paths.append(tempPath)

def findAllPath():
    paths = [["start"]]
    addRoute(paths)
    addEnd(paths)
    paths = [path for path in paths if path[-1] == "end"]
    return(paths)

paths = findAllPath()
print(paths)
print(len(paths))

diff = [x for x in outputs if x not in paths]
print(diff)