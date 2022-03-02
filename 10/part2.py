def getInput(file):
    # input = []
    with open(file) as f:
        data = f.read().splitlines()

    # for line in data:
    #     temp = [char for char in line]
    #     input.append(temp)

    return data

inputs = getInput("input.txt")

print(inputs)

def isCorrupted(line):
    stack = []
    for char in line:
        if char == "(" or char == "[" or char == "{" or char == "<":
            stack.append(char)
        elif char == ")" and stack[-1] != "(":
            # print(line)
            return True
        elif char == "]" and stack[-1] != "[":
            # print(line)
            return True
        elif char == "}" and stack[-1] != "{":
            # print(line)
            return True
        elif char == ">" and stack[-1] != "<":
            # print(line)
            return True
        else:
            stack.pop()

def removeCorruptedLines(inputs):
    uncorruptedLines = [line for line in inputs if not isCorrupted(line)]

    return(uncorruptedLines)
    

uncorruptedLines = removeCorruptedLines(inputs)
print(len(uncorruptedLines))
print(uncorruptedLines)

def fixLine(line):
    stack = []
    for char in line:
        if char == "(" or char == "[" or char == "{" or char == "<":
            stack.append(char)
        else:
            stack.pop()
    
    score = 0
    for char in reversed(stack):
        score *= 5
        if char == "(":
            score += 1
            line += ")"
        elif char == "[":
            score += 2
            line += "]"
        elif char == "{":
            score += 3
            line += "}"
        elif char == "<":
            score += 4
            line += ">"

    return score

def calculateScore(uncorruptedLines):
    scores = []
    for line in uncorruptedLines:
        scores.append(fixLine(line))
    
    scores.sort()
    print(scores)
    return scores[int((len(scores)-1)/2)]

middleScore = calculateScore(uncorruptedLines)
print(middleScore)