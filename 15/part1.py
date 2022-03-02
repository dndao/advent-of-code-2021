import math
import copy

def getInput(file):
    with open(file) as f:
        data = f.read().splitlines()

    inputs = []
    for line in data:
        inputs.append([char for char in line])

    return(inputs)

inputs = getInput("testinput.txt")
print(inputs)

unvisited = []
riskMap = []
distances = []

for i in range(len(inputs)):
    temp = []
    for j in range(len(inputs[0])):
        riskMap.append((i,j))
        temp.append(math.inf)
    distances.append(temp)
    distances[0][0] = 0

unvisited = copy.deepcopy(riskMap)

print(unvisited)
print(distances)

def calculateDistanceToVertices(row, col):
    # get list of vertices
    # distance from A to vertices = distance from A to node + value of vertices
    # update value is distances, remove node from unvisited.
    vertices = []
    if riskMap[]
    pass


def findLowestTotalRisk(riskMap):
    while len(unvisited) > 0:
        # calculateDistanceToVertices() for smallest value in distances that is unvisited 
    

