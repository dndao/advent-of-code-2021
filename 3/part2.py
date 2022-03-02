from varname import nameof

with open('testinput.txt') as f:
    input = f.read().splitlines()

print(input)

def whatToRemove(digit, system, surviveList):
    count0 = 0
    count1 = 0
    for index in range(len(input)):
        if index in surviveList:
            if input[index][digit] == "0":
                count0 += 1
            if input[index][digit] == "1":
                count1 += 1

    if system == "oxygen":
        if count0 > count1:
            return "1"
        elif count1 > count0:
            return "0"
        elif count1 == count0:
            return "0"
    elif system == "co2":
        if count0 > count1:
            return "0"
        if count1 > count0:
            return "1"
        if count1 == count0:
            return "1"

def calculateSupport(system):
    surviveList = list(range(len(input)))
    for digit in range(len(input[0])):
        removeDigit = whatToRemove(digit, system, surviveList)
        for index in range(len(input)):
            if index in surviveList:
                if input[index][digit] == removeDigit and len(surviveList) > 1:
                    surviveList.remove(index)
    
    res = int(input[surviveList[0]], 2)
    print("Last value for ",system," is:", res)
    return res

oxyRes = calculateSupport("oxygen")
co2Res = calculateSupport("co2")
print(oxyRes*co2Res)