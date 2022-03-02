with open('input.txt') as f:
    input = f.read().splitlines()

length = 0
depth = 0

# print(input)

# part 1
for x in range(0, len(input)):
    command, value = str(input[x]).split()
    if "forward" == command:
        length+= int(value)
    if "down" == command:
        depth+= int(value)
    if "up" == command:
        depth-= int(value)

print(length*depth)

length = 0
depth = 0
aim = 0

# part 2
for x in range(0, len(input)):
    command, value = str(input[x]).split()
    if "forward" == command:
        length+= int(value)
        depth+= (aim*int(value))
    if "down" == command:
        aim+= int(value)
    if "up" == command:
        aim-= int(value)

print(input)
print(length, " and ", depth)
print(length*depth)