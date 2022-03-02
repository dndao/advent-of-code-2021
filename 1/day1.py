with open('input.txt') as f:
    input = f.read().splitlines()

count = 0

for x in range(1, len(input)):
    if int(input[x]) > int(input[x-1]):
        count+=1

print("The number of measurements that are larger than the previous measurement is", count)

count = 0
for x in range(1, len(input)-2):
    # print (int(input[x-1]) + int(input[x]) + int(input[x+1]), " and ", int(input[x]) + int(input[x+1]) + int(input[x+2]))
    if int(input[x-1]) + int(input[x]) + int(input[x+1]) < int(input[x]) + int(input[x+1]) + int(input[x+2]):
        count+=1

print("The number of sums are larger than the previous sum is", count)
