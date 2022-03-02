def getSchool(file):
    with open(file) as f:
        input = f.read().splitlines()
        input = [int(s) for s in input[0].split(",")]

    return input

fishSchool = getSchool("testinput2.txt")

schoolSize = [len(fishSchool)]


def growSchool(school):
    for i in range(len(school)):
        if school[i] == 0:
            school[i] = 7
            school.append(8)
        if school[i] <= 8 and school[i] != 0:
            school[i] -= 1    
    
    schoolSize.append(len(school))
    return school

def stimulateGrowSchool(school, days):

    for day in range(days):
        school = growSchool(school)

    return len(school)     

fishNumber = stimulateGrowSchool(fishSchool, 100)
print(schoolSize)

difference = []
for n in range(len(schoolSize)-1):
    difference.append(schoolSize[n+1] - schoolSize[n])

print(difference)
