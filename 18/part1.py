import copy

def getHomework(file):
    with open(file) as f:
        amphipods = f.read().splitlines()
    
    return(amphipods)

homework = getHomework("testinput.txt")

def addition(current, pairNumber):
    # add pair
    temp = "[" + current + "," + pairNumber + "]"
    checkExplode(temp)
    # explore and if explorable
    return(temp)

def explode(pairNumber, index):
    # perform explode
    explodedPair = pairNumber[index:index+5]
    i = index
    leftDigitIndex = -1
    rightDigitIndex = 0
    while (i != 0):
        if pairNumber[i].isdigit():
            leftDigitIndex = i
            break
        i -= 1
    if (leftDigitIndex != -1):
        leftDigit = str(int(pairNumber[leftDigitIndex]) + int(pairNumber[index+1]))
    i = index
    while (i != (len(pairNumber) - 1)):
        if pairNumber[i].isdigit():
            rightDigitIndex = i
            break
        i += 1
    if (rightDigitIndex != 0):
        rightDigit = str(int(pairNumber[rightDigitIndex]) + int(pairNumber[index+3]))

    if (leftDigitIndex and not rightDigitIndex):
        temp = pairNumber[0:leftDigitIndex] + leftDigit + pairNumber[leftDigitIndex+1:index] + "0" + pairNumber[index+5:]
    if (rightDigitIndex and not leftDigitIndex):
        temp = pairNumber[0:index] + "0" + pairNumber[index+5:rightDigitIndex-1] + rightDigit + pairNumber[rightDigitIndex+1:]
    if (leftDigitIndex and rightDigitIndex):
        temp = pairNumber[0:leftDigitIndex] + leftDigit + pairNumber[leftDigitIndex+1:index] + "0" + pairNumber[index+5:rightDigitIndex-1] + rightDigit + pairNumber[rightDigitIndex+1:]
    # check explodable
    print(temp)
    checkExplode(temp)

def split():
    # perform split
    # check explodable
    pass

def checkSplit(pairNumber):
    # if splitable
    # split(pairNumber)
    # if not
    # do nothing
    return

def checkExplode(pairNumber):
    # if explorable:
    # explode(pairNumber)
    count = 0
    for i in range(len(pairNumber)):
        if pairNumber[i] == "[":
            count += 1
        if pairNumber[i] == "]":
            count -= 1
        if count == 5:
            # find next left and add left value to that value
            # find the next right and add right value to that value
            # replace  pair with 0
            pairNumber = explode(pairNumber, i)
    # if not
    # checkSplit(pairNumber)
    checkSplit(pairNumber)

def findSum(homework):
    current = homework[0]
    for i in range(1, len(homework)):
        current = addition(current, homework[i])

addition(homework[0], homework[1])