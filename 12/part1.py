import copy

def getInput(file):
    input = []
    with open(file) as f:
        data = f.read().splitlines()

    for line in data:
        temp = (line.split("-")[0],line.split("-")[1])
        input.append(temp)

    return input

inputs = getInput("input.txt")

def createDictionary(inputs):
    routeDict = {}
    for input in inputs:
        if input[0] in routeDict:
            routeDict[input[0]].append(input[1])
        else:
            routeDict[input[0]] = []
            routeDict[input[0]].append(input[1])
        if input[1] in routeDict:
            routeDict[input[1]].append(input[0])
        else:
            routeDict[input[1]] = []
            routeDict[input[1]].append(input[0])
    
    for key in routeDict.keys():
        if key != "start" or key != "end":
            if "start" in routeDict[key]:
                routeDict[key].remove("start")
    
    return(routeDict)

routeDict = createDictionary(inputs)
print(routeDict)

def addRoute(paths):
    for path in paths:
        if path[-1] != "end":
            for value in routeDict[path[-1]]:
                tempPath = copy.deepcopy(path)
                if value.islower() and value not in tempPath:
                    tempPath.append(value)
                    if tempPath not in paths:
                        paths.append(tempPath)
                if value.isupper():
                    tempPath.append(value)
                    if tempPath not in paths:
                        paths.append(tempPath)

def findAllPath():
    paths = []
    path = ["start"]
    paths.append(path)
    addRoute(paths)

    paths = [path for path in paths if path[-1] == "end"]
    return(paths)

paths = findAllPath()
print(paths)
print(len(paths))