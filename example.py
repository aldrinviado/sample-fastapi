


import typing




num = int(input("How many rows do you like to enter?"))

for i in range(num):
    for j in range(i+1):
        print("*",end="")
    print()


for i in range(num):
    for j in range(i,num-1):
        print("*",end="")
    print()