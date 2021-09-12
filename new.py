import random
f = open("documents/sumall.txt")

line = f.readline()
x = 0
valueAll = []
while line:
    # print(line)
    templist = line.split(", ")
    line = f.readline()
    # print(templist)
    for i in templist:
        valueAll.append(int(i))
print(valueAll)
list = []
listAll = []
sum = 0
sumAll = []
for y in range(1,25):
    for x in range(1,9):
        allValue = random.randint(0,6000)
        list.append(allValue)
        sum = sum + allValue
    sumAll.append(sum)
    list.sort(reverse=True)
    listAll.append(list)
    list = []
    sum  = 0
print(listAll)
print(sumAll)
# i = 0
# for i in range(len(sumAll)):
#     sub = valueAll.index(i) - sumAll.index(i)
#     print(type(valueAll.index(1)))
