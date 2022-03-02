def getInput(file):
    with open(file) as f:
        data = f.read().splitlines()
        print(data)
        output = []
        for value in data:
            output.append(value.split(" | ")[1])

    return output

output = getInput("input.txt")

print(output)

count = 0
for value in output:
    print(value)
    temp = value.split(" ")
    for string in temp:
        if len(string) == 2 or len(string) == 3 or len(string) == 4 or len(string) == 7:
            count += 1

print(count)