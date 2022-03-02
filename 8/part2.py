def getInputOutput(file):
    with open(file) as f:
        data = f.read().splitlines()
        output = []
        input = []
        for value in data:
            output.append(value.split(" | ")[1])
            input.append(value.split(" | ")[0])

    return input, output

inputs, outputs = getInputOutput("input.txt")

def getCues(input):
        numbers = input.split(" ")
        twoThreeFive = []
        zeroSixNine = []
        for string in numbers:
            if len(string) == 2:
                one = string
            elif len(string) == 3:
                seven = string
            elif len(string) == 4:
                four = string
            elif len(string) == 7:
                eight = string
            elif len(string) == 5:
                twoThreeFive.append(string)
            elif len(string) == 6:
                zeroSixNine.append(string)
        if one and seven and four and eight and twoThreeFive and zeroSixNine:
            return one, seven, four, eight, twoThreeFive, zeroSixNine
        else: 
            return None

def findACF(one, seven, zeroSixNine, displayMap):
    cf = []
    for c in seven:
        if c not in one:
            # print(c)
            # print(one)
            # print(seven)
            displayMap["a"] = c
        else:
            cf.append(c)

    for number in zeroSixNine:
        for digit in cf:
            if digit not in number:
                displayMap["c"] = digit

    for c in seven:
        if c != displayMap["c"] and c != displayMap["a"]:
            # print(c)
            displayMap["f"] = c
    
def findGDBE(twoThreeFive, four, eight, displayMap):
    for number in twoThreeFive:
        if displayMap["f"] in number and displayMap["c"] in number:
            three = number

    dg = []
    for c in three:
        if c != displayMap["c"] and c != displayMap["a"] and c != displayMap["f"]:
            dg.append(c)

    for c in dg:
        if c not in four:
            # print(c)
            displayMap["g"] = c
        else:
            displayMap["d"] = c

    for c in four:
        if c != displayMap["c"] and c != displayMap["d"] and c != displayMap["f"]:
            # print(c)
            displayMap["b"] = c
    
    for c in eight:
        if c != displayMap["c"] and c != displayMap["d"] and c != displayMap["f"] and c != displayMap["a"] and c != displayMap["b"] and c != displayMap["g"]:
            # print(c)
            displayMap["e"] = c

def translate(output, displayMap):
    hiddenNumber = ""
    numbers = output.split(" ")
    for string in numbers:
        temp = ""
        if len(string) == 2:
            temp = "1"
        elif len(string) == 3:
            temp = "7"
        elif len(string) == 4:
            temp = "4"
        elif len(string) == 7:
            temp = "8"
        elif len(string) == 5 and displayMap["c"] in string and displayMap["f"] in string:
            temp = "3"
        elif len(string) == 5 and displayMap["c"] in string and displayMap["f"] not in string:
            temp = "2"
        elif len(string) == 5 and displayMap["c"] not in string and displayMap["f"] in string:
            temp = "5"
        elif len(string) == 6 and displayMap["d"] not in string:
            temp = "0"
        elif len(string) == 6 and displayMap["c"] not in string:
            temp = "6"
        elif len(string) == 6 and displayMap["e"] not in string:
            temp = "9"
        else:
            print(string)
            print(displayMap)
        hiddenNumber += temp

    return hiddenNumber
    

def solveInputs():
    sum = 0
    for i in range(len(inputs)):
        one, seven, four, eight, twoThreeFive, zeroSixNine = getCues(inputs[i])

        displayMap = {
            "a" : "",
            "b" : "",
            "c" : "",
            "d" : "",
            "e" : "",
            "f" : "",
            "g" : ""
        }
        
        findACF(one, seven, zeroSixNine, displayMap)
        findGDBE(twoThreeFive, four, eight, displayMap)

        value = translate(outputs[i], displayMap)
        print(outputs[i],":",value)
        sum += int(value)

    print(sum)

solveInputs()