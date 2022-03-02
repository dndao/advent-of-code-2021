def getSchool(file):
    with open(file) as f:
        input = f.read().splitlines()
        input = [int(s) for s in input[0].split(",")]

    return input

fishSchool = getSchool("testinput2.txt")

print(len(fishSchool))
print(fishSchool)
schools = []

for i in range(int(len(fishSchool)/3)):
    temp = []
    for j in range(3):
        temp.append(fishSchool[i*3+j])
    schools.append(temp)

print(schools)
print(len(schools))

schoolSize = [len(fishSchool)]

def growSchool(school):
    for i in range(len(school)):
        if school[i] == 0:
            school[i] = 7
            school.append(8)
        if school[i] <= 8 and school[i] != 0:
            school[i] -= 1    
    # for fish in school:

    schoolSize.append(len(school))

    return school

def stimulateGrowSchool(school, days):

    for day in range(days):
        # if (day == 0):
        #     pass
        #     # print("Initial state: ", end="")
        # else:
        #     # print("After ", day, " days: ", end="")
        #     pass
        
        for school in schools:
            school = growSchool(school)
        # for fish in school:
            # print(fish," ", end="")
        # print()

    return len(schools)

stimulateGrowSchool(fishSchool, 256)

schoolSize = 0
for school in schools:
    schoolSize += len(school)

fishNumber = stimulateGrowSchool(fishSchool, 80)
print(fishNumber)
print(schoolSize)