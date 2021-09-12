import random

# f = open("documents/sumall.txt")

# line = f.readline()
# x = 0
# while line:
#     # print(line)
#     templist = line.split(", ")
#     line = f.readline()
#     # print(templist)
#     for i in templist:
#         print(i)


sum =0
Temp = []

def loop():
    for x in range(0,50):
        value = random.randint(0,6000)
        global sum
        global Temp
        Temp.append(value)
        sum = value + sum

    if sum <=6000:
        print(Temp)
    else:
        loop()


loop()

