import sys

def getBinary(file):
    with open(file) as f:
        hexStr = f.read()

    h_size = len(hexStr) * 4
    binary = (bin(int(hexStr, 16))[2:]).zfill(h_size)

    return(binary)

binaryStr = getBinary(sys.argv[1])

def getVersion(binary):
    return(int(binary[:3],2))

def getTypeID(binary):
    return(int(binary[3:6],2))

def getValue(binary):
    valueStr = binary[6:]
    intStr = ""
    for x in range(int(len(valueStr)/5)):
        if valueStr[5*x:5*x+5][1] == 0:
            intStr += valueStr[5*x:5*x+5][1:]
            return(int(intStr,2)) 
        else:
            intStr += valueStr[5*x:5*x+5][1:]

    return(int(intStr,2))

def getLengthTypeID(binary):
    return(int(binary[6],2))

def getTrunk(binary):
    if getTypeID(binary) == 4:
        headerStr = binary[0:6]
        leftPart = binary[6:]
        valueStr = ""
        for x in range(int(len(leftPart)/5)):
            if leftPart[5*x:5*x+5][1] == 0:
                valueStr += leftPart[5*x:5*x+5]
                break
            else:
                valueStr += leftPart[5*x:5*x+5]

        trunk = headerStr + valueStr
        binary = binary[len(trunk):]
    else:
        if getLengthTypeID(binary) == 0:
            headerStr = binary[0:6]
            bitCount = int(binary[7:22],2)
            print("Length of the sub-packets in bits: ", bitCount)
            valueStr = binary[22:22+bitCount]
            trunk = headerStr + valueStr
            binary = binary[len(trunk):]
        elif getLengthTypeID(binary) == 1:
            headerStr = binary[0:6]
            packagesCount = int(binary[7:18],2)
            print("Number of sub-packets: ", packagesCount)
            subpackages = binary[18:]
            print(subpackages)
    return(trunk, binary)

versionCount = 0

def decodeBinary(binary):
    global versionCount
    print(binary)
    if getTypeID(binary) == 4:
        print("Version: ", getVersion(binary))
        print("Type ID: ", getTypeID(binary))
        print("Value: ", getValue(binary))
        versionCount += getVersion(binary)
    else:
        print("Version: ", getVersion(binary))
        print("Type ID: ", getTypeID(binary))
        print("Length Type ID: ", getLengthTypeID(binary))
        versionCount += getVersion(binary)
        if getLengthTypeID(binary) == 0:
            bitCount = int(binary[7:22],2)
            print("Length of the sub-packets in bits: ", bitCount)
            subpackages = binary[22:22+bitCount]
            if len(subpackages) >= 11:
                if getTypeID(subpackages) == 4:
                    packagesArr = []
                    for x in range(int(len(subpackages)/11)):
                        subpackage = subpackages[11*x:11*x+11]
                        packagesArr.append(subpackage)
                    if len(subpackages)%11 != 0:
                        packagesArr.append(subpackages[-(len(subpackages)%11):])
                    if packagesArr != []:
                        if (len(packagesArr[-1]) < 11):
                            packagesArr[-2] = packagesArr[-2] + packagesArr[-1]
                            packagesArr.pop()
                    for package in packagesArr:
                        decodeBinary(package)
                else:
                    decodeBinary(subpackages)
        elif getLengthTypeID(binary) == 1:
            packagesCount = int(binary[7:18],2)
            print("Number of sub-packets: ", packagesCount)
            subpackages = binary[18:]
            print(subpackages)
            if len(subpackages) >= 11:
                if getTypeID(subpackages) == 4:
                    packagesArr = []
                    i = 0
                    while packagesCount > 0:
                        subpackage = subpackages[11*i:11*i+11]
                        packagesArr.append(subpackage)
                        print(packagesCount)
                        i += 1
                        packagesCount -= 1
                    print(packagesArr)
                    for package in packagesArr:
                        decodeBinary(package)
                else:
                    decodeBinary(subpackages)

decodeBinary(binaryStr)
print(versionCount)

testStr="11101110000000001101010000001100100000100011000001100000"
print(testStr)
testTrunk, testBinary = getTrunk(testStr)
print(testTrunk)
print(testBinary)