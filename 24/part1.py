import copy

def getInstructions(file):
    with open(file) as f:
        instructions = f.read().splitlines()

    # monad = []
    # for row in instructions:
    #     monad.append([cCB for cCB in row])
    
    return(instructions)

MONAD = getInstructions("monad.txt")

w, x, y, z = 0, 0, 0, 0

def proper_round(num, dec=0):
    num = str(num)[:str(num).index('.')+dec+2]
    if num[-1]>='5':
        return float(num[:-2-(not dec)]+str(int(num[-2-(not dec)])+1))
    return float(num[:-1])

def inp(a, num):
    globals()[a] = num

def add(a, b):
    if b.lstrip('-').isdigit():
        globals()[a] = globals()[a] + int(b)
    else:
        globals()[a] = globals()[a] + globals()[b]

def mul(a, b):
    if b.lstrip('-').isdigit():
        globals()[a] = globals()[a] * int(b)
    else:
        globals()[a] = globals()[a] * globals()[b]

def div(a, b):
    if b.lstrip('-').isdigit():
        globals()[a] = int(proper_round(globals()[a] / int(b)))
    else:
        globals()[a] = int(proper_round(globals()[a] / globals()[b]))

def mod(a, b):
    if b.lstrip('-').isdigit():
        globals()[a] = globals()[a] % int(b)
    else:
        globals()[a] = globals()[a] % globals()[b]

def eql(a, b):
    if b.lstrip('-').isdigit():
        if globals()[a] == int(b):
            globals()[a] = 1
        else:
            globals()[a] = 0
    else:
        if globals()[a] == globals()[b]:
            globals()[a] = 1
        else:
            globals()[a] = 0

def computeInstruction(instruct, modelNum):
    operation = instruct[0:3]
    match operation:
        case "inp":
            a = instruct[4:5]
            inp(a, int(modelNum[globals()['cur']]))
            globals()['cur'] += 1
        case "add":
            a = instruct[4:5]
            b = instruct[6:]
            add(a,b)
        case "mul":
            a = instruct[4:5]
            b = instruct[6:]
            mul(a,b)
        case "div":
            a = instruct[4:5]
            b = instruct[6:]
            div(a,b)
        case "mod":
            a = instruct[4:5]
            b = instruct[6:]
            mod(a,b)
        case "eql":
            a = instruct[4:5]
            b = instruct[6:]
            eql(a,b)

# model = "13579246899999"
# start = "10000000000000"
# end = "99999999999999"

# for number in range(10000000000000, 100000000000000):
#     if "0" not in str(number):
#         print(number)
#         # for instruct in MONAD:
#         #     computeInstruction(instruct, str(x))

# print(z)

found = False
model = 99999999999999
while (not found):
    if "0" not in str(model):
        print(model)
        for instruct in MONAD:
            computeInstruction(instruct, str(model))
        if z == 0:
            found = True
    model -= 1
