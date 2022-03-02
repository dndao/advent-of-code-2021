def getVeins(file):
    with open(file) as f:
        input = f.read().splitlines()

    veins = []

    for value in input:
        # translate to coordinate
        temp = []

        startRaw = value[0:value.find("->")]
        start = (int(startRaw.split(",")[0]),int(startRaw.split(",")[1]))
        endRaw = value[value.find("->")+2:len(value)]
        end = (int(endRaw.split(",")[0]),int(endRaw.split(",")[1]))

        if (start[0] == end[0]):
            if (start[1] > end[1]):
                for x in range(start[1]-end[1]+1):
                    temp.append((start[0],end[1]+x))
            if (start[1] < end[1]):
                for x in range(end[1]-start[1]+1):
                    temp.append((start[0],start[1]+x))
        elif (start[1] == end[1]):
            if (start[0] > end[0]):
                for x in range(start[0]-end[0]+1):
                    temp.append((end[0]+x,start[1]))
            if (start[0] < end[0]):
                for x in range(end[0]-start[0]+1):
                    temp.append((start[0]+x,start[1]))
        else:
            if (start[1] > end[1]) and (start[0] > end[0]):
                for x in range(start[1]-end[1]+1):
                    temp.append((start[0]-x,start[1]-x))
            if (start[1] > end[1]) and (start[0] < end[0]):
                for x in range(start[1]-end[1]+1):
                    temp.append((start[0]+x,start[1]-x))
            if (start[1] < end[1]) and (end[0] < start[0]):
                for x in range(end[1]-start[1]+1):
                    temp.append((start[0]-x,start[1]+x)) 
            if (start[1] < end[1]) and (start[0] < end[0]):
                for x in range(end[1]-start[1]+1):
                    temp.append((start[0]+x,start[1]+x)) 

        if (temp != []):
            veins.append(temp)

    return veins

veins = getVeins("input.txt")


def drawMap(rows, cols):
    
    veinsMap = []
    for i in range(rows):
        new = []
        for j in range(cols):
            new.append(0)
        veinsMap.append(new)
    
    for row in veins:
        for val in row:
            veinsMap[val[1]][val[0]] += 1
    
    for row in veinsMap:
        for val in row:
            print(val, end="")
        print("\n")

    count = 0
    for row in veinsMap:
        for val in row:
            if (val > 1):
                count += 1
    
    print(count)

drawMap(1000,1000)