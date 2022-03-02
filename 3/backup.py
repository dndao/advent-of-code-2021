with open('input.txt') as f:
    input = f.read().splitlines()

oxygen = input.copy()
co2 = input.copy()

def whatToRemove(position, values, type, surviveList):
    count0 = 0
    count1 = 0
    for index in range(len(values)):
        if index in surviveList:
            if values[index][position] == "0":
                count0 += 1
            elif values[index][position] == "1":
                count1 += 1

    if type == "oxygen":
        if count0 > count1:
            return "1"
        elif count1 > count0:
            return "0"
        elif count1 == count0:
            return "0"
    if type == "co2":
        if count0 > count1:
            return "0"
        elif count1 > count0:
            return "1"
        elif count1 == count0:
            return "1"  

def calculateSupport(values, type):
    surviveList = list(range(len(values)))
    print("Calculating: ", type)
    for digit in range(len(values[0])):
        for index in range(len(values)):
            if index in surviveList:
                if values[index][digit] == whatToRemove(digit, values, type, surviveList) and len(surviveList) > 1:
                    surviveList.remove(index)
    print(int(values[surviveList[0]],2))
    return(surviveList[0])


oxygenPos = calculateSupport(oxygen, "oxygen")
co2Pos = calculateSupport(co2, "co2")
print(int(co2[co2Pos],2) * int(oxygen[oxygenPos],2))
