import copy

def getMap(file):
    with open(file) as f:
        amphipods = f.read().splitlines()
    
    return(amphipods)

amphipods = getMap("testinput.txt")
print(amphipods)