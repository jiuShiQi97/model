import random

Temp = []
sum = 0
# for x in range(0,50):
#     value = random.randint(0,6000)
#     Temp.append(value)
# print(Temp)
while 1:
    value = random.randint(0,6000)
    Temp.append(value)
    sum = sum+value
    if sum == 6000:
        print(Temp)
        break
    elif sum > 6000:
        sum = 0
        Temp = []