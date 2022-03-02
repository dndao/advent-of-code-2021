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

def getIncorrect(line):
    stack = []
    for char in line:
        if char == "(" or char == "[" or char == "{" or char == "<":
            stack.append(char)
        elif char == ")" and stack[-1] != "(":
            return char
        elif char == "]" and stack[-1] != "[":
            return char
        elif char == "}" and stack[-1] != "{":
            return char
        elif char == ">" and stack[-1] != "<":
            return char
        else:
            stack.pop()

def calculateScore(inputs):
    score = 0
    for line in inputs:
        incorrect = getIncorrect(line)
        if incorrect == ")":
            score += 3
        elif incorrect == "]":
            score += 57
        elif incorrect == "}":
            score += 1197
        elif incorrect == ">":
            score += 25137
    
    return score

score = calculateScore(inputs)

print(score)