with open('input.txt') as f:
    input = f.read().splitlines()

print(input)

bitList = [""] * len(input[0])
gamma = ""
epsilon = ""

print(bitList)

for x in range(len(bitList)):
    for value in input:
        bitList[x] += value[x]

print(bitList)

for x in bitList:
    count0 = 0
    count1 = 0
    for c in x:
        if c == "0":
            count0 += 1
        else:
            count1 += 1
    if count0 > count1:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += '0'

print(gamma)
print(epsilon)
print(int(gamma, 2)*int(epsilon, 2))



    