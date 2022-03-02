with open('calls.txt') as f:
    calls = f.read().splitlines()

calls = calls[0].split(",")

print(calls)

def setUpBoard(file):
    with open(file) as f:
        rawBoards = f.read().splitlines()

    boards = []

    for x in range(int(len(rawBoards)/6)):
        temp = [None] * 5
        temp[0] = rawBoards[x*6]
        temp[1] = rawBoards[x*6+1]
        temp[2] = rawBoards[x*6+2]
        temp[3] = rawBoards[x*6+3]
        temp[4] = rawBoards[x*6+4]
        boards.append(temp)

    for x in range(len(boards)):
        temp = [None] * 5
        temp[0] = [str(s) for s in boards[x][0].split() if s.isdigit()]
        temp[1] = [str(s) for s in boards[x][1].split() if s.isdigit()]
        temp[2] = [str(s) for s in boards[x][2].split() if s.isdigit()]
        temp[3] = [str(s) for s in boards[x][3].split() if s.isdigit()]
        temp[4] = [str(s) for s in boards[x][4].split() if s.isdigit()]
        boards[x] = temp

    return boards

boards = setUpBoard("boards.txt")

def markCall(board, call):
    for row in board:
        if row[0] == call:
            row[0] += "x"
        if row[1] == call:
            row[1] += "x"
        if row[2] == call:
            row[2] += "x"
        if row[3] == call:
            row[3] += "x"
        if row[4] == call:
            row[4] += "x"

    for col in range(5):
        if board[0][col] == call:
            board[0][col] += "x"
        if board[1][col] == call:
            board[1][col] += "x"
        if board[2][col] == call:
            board[2][col] += "x"
        if board[3][col] == call:
            board[3][col] += "x"
        if board[4][col] == call:
            board[4][col] += "x"

def checkBingo(board):
    for row in board:
        if "x" in row[0] and "x" in row[1] and "x" in row[2] and "x" in row[3] and "x" in row[4]:
            return True
    for col in range(5):
        if "x" in board[0][col] and "x" in board[1][col] and "x" in board[2][col] and "x" in board[3][col] and "x" in board[4][col]:
            return True
    return False

def calculateScore(board, lastCall):
    print("Calculating score:....")
    score = 0
    for row in board:
        if "x" not in row[0]:
            score += int(row[0])
        if "x" not in row[1]:
            score += int(row[1])
        if "x" not in row[2]:
            score += int(row[2])
        if "x" not in row[3]:
            score += int(row[3])
        if "x" not in row[4]:
            score += int(row[4])
    return score * int(lastCall)

# foundWinner = False
winnerList = []
for call in calls:
    for n in range(len(boards)):
        if n not in winnerList:
            markCall(boards[n], call)
            # Check board if winning
            if (checkBingo(boards[n])):
                print(boards[n])
                print(calculateScore(boards[n], call))
                winnerList.append(n)
    #             foundWinner = True
    #             break
    # if foundWinner:
    #     break

print(winnerList)
print(len(winnerList))