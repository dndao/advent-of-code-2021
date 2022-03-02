def getPositions(file):
    with open(file) as f:
        input = f.read().splitlines()
        input = [int(s) for s in input[0].split(",")]

    return input

positions = getPositions("input.txt")

print(positions)

def findSum(n):
    sum = 0
    for i in range(n):
        sum += i

    return sum

def findCheapestMove(positions):
    moves = []
    for i in range(len(positions)):
        cost = 0
        for position in positions:
            cost += abs(position - i)
            cost += findSum(abs(position - i))
        moves.append(cost)

    for index in range(len(moves)):
        if moves[index] == min(moves):
            return moves[index]

print(findCheapestMove(positions))
