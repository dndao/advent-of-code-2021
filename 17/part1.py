import sys
import math

def getRange(file):
    with open(file) as f:
        targetRange = f.read()
    print(targetRange)

    xRange = (int(targetRange[targetRange.find("x=")+2:targetRange.find('..')]),int(targetRange[targetRange.find("..")+2:targetRange.find(',')]))
    temp = targetRange[targetRange.find("y="):]
    yRange = (int(temp[temp.find("y=")+2:temp.find("..")]), int(temp[temp.find("..")+2:len(temp)]))

    return([xRange, yRange])

targetRange = getRange(sys.argv[1])

def findStep(targetRange):
    sumLow = 0
    low = 0
    while sumLow < targetRange[0][0]:
        sumLow+= low
        low+=1

    sumHigh = 0
    high = 0
    while sumHigh < targetRange[0][1]:
        sumHigh+= high
        high+=1
    
    return(low-1,high-2)

stepRange = findStep(targetRange)
print(stepRange)

def stimulate(targetRange, stepRange):
    yMax = 0
    for step in stepRange:
        for y in range(10):
            testY = y
            for i in range(step):
                testY -= 1
            print(testY)
            if testY >= targetRange[1][0] and testY <= targetRange[1][1]:
                print("candidate: ",y)
                if y > yMax:
                    yMax = y
    # print(yMax)

stimulate(targetRange, stepRange)