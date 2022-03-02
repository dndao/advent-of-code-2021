def getSchool(file):
    with open(file) as f:
        input = f.read().splitlines()
        input = [int(s) for s in input[0].split(",")]

    return input

fishSchool = getSchool("testinput.txt")

def growSchool(school):
    for i in range(len(school)):
        if school[i] == 0:
            school[i] = 7
            school.append(8)
        if school[i] <= 8 and school[i] != 0:
            school[i] -= 1    

    return school

def stimulateGrowSchool(school, days):

    for day in range(days):
        # if (day == 0):
        #     print("Initial state: ", end="")
        # else:
        #     print("After ", day, " days: ", end="")
        school = growSchool(school)
        # for fish in school:
        #     print(fish," ", end="")
        # print()

    return len(school)     

fishNumber = stimulateGrowSchool(fishSchool, 80)
print(fishNumber)