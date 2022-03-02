import sys
import copy

def getImage(file):
    with open(file) as f:
        inputs = f.read().splitlines()

    algorithm = inputs[0]
    image = []
    for line in inputs[2:]:
        image.append([pixel for pixel in line])
    
    return algorithm, image

algorithm, image = getImage(sys.argv[1])

def padImage2(image):
    paddedImage = []
    newRow = ['.'] * (len(image[0]) + 4)
    paddedImage.append(newRow)
    paddedImage.append(newRow)
    for line in image:
        tempLine = ['.','.']
        for pixel in line:
            tempLine.append(pixel)
        tempLine.append('.')
        tempLine.append('.')
        paddedImage.append(tempLine)
    paddedImage.append(newRow)
    paddedImage.append(newRow)

    return paddedImage

def padImage1(image):
    paddedImage = []
    newRow = ['.'] * (len(image[0]) + 2)
    paddedImage.append(newRow)
    for line in image:
        tempLine = ['.']
        for pixel in line:
            tempLine.append(pixel)
        tempLine.append('.')
        paddedImage.append(tempLine)
    paddedImage.append(newRow)

    return paddedImage

def calculatePixel(pixelIndex, currentImage):
    binaryArry = []

    pad2 = padImage2(currentImage)

    # loop first line
    for pixel in pad2[pixelIndex[0]][pixelIndex[1]:pixelIndex[1]+3]:
        if pixel == ".":
            binaryArry.append('0')
        elif pixel == "#":
            binaryArry.append('1')
    # loop second line
    for pixel in pad2[pixelIndex[0]+1][pixelIndex[1]:pixelIndex[1]+3]:
        if pixel == ".":
            binaryArry.append('0')
        elif pixel == "#":
            binaryArry.append('1')
    # loop third line
    for pixel in pad2[pixelIndex[0]+2][pixelIndex[1]:pixelIndex[1]+3]:
        if pixel == ".":
            binaryArry.append('0')
        elif pixel == "#":
            binaryArry.append('1')
    
    binary = ''.join(binaryArry)
    decimal = int(binary,2)
    # print(decimal)

    return algorithm[decimal]

def enhance(image):
    newImage = []

    pad1 = padImage1(image)

    for row in range(len(pad1)):
        newLine = []
        for col in range(len(pad1[0])):
            # Enhance this pixel
            newPixel = calculatePixel((row,col), image)
            newLine.append(newPixel)
        newImage.append(newLine)
    
    return newImage

for i in range(2):
    image = enhance(image)
    for line in image:
        for pixel in line:
            print(pixel, end="")
        print("")
    print("=========")

count = 0
for line in image:
    for pixel in line:
        if pixel == "#":
            count += 1

print(count)