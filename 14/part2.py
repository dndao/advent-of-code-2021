import copy

def getInput(file):
    with open(file) as f:
        data = f.read().splitlines()

    startString = ""
    rules = {}

    for line in data:
        if "->" in line:
            key = line.split(" -> ")[0]
            value = line.split(" -> ")[1]
            rules[key] = value
        elif "->" not in line and line != "":
            startString = line

    return startString, rules

startString, rules = getInput("testinput.txt")

def growString(startString):
    tempArr = []
    newString = startString[0]
    for i in range(len(startString) - 1):
        tempKey = startString[i] + startString[i+1]
        if tempKey in rules.keys():
            tempArr.append(rules[tempKey])
            newString += ("." + startString[i+1])
        else:
            newString += (startString[i+1])    

    x = 0
    for char in newString:
        if char == ".":
            newString = newString.replace(".",tempArr[x],1)
            x += 1
    
    countDict = {}
    totalDict = 0
    for key in rules.keys():
        countDict[key] = newString.count(key)
        totalDict += newString.count(key)
    
    countCharDict = {}
    totalCharDict = 0
    charCountArr = []
    for char in set(newString):
        countCharDict[char] = newString.count(char)
        charCountArr.append(countCharDict[char])
        totalCharDict += countCharDict[char]

    print(countCharDict, totalCharDict, "max-min: ", max(charCountArr)-min(charCountArr))
    # print(countDict, totalDict)
    return(newString)

def growStringSteps(startString, steps):
    for step in range(steps):
        startString = growString(startString)

    countChars = []
    for char in set(startString):
        countChars.append(startString.count(char))

    # print(countChars)
    # print(max(countChars) - min(countChars))

growStringSteps(startString, 18)