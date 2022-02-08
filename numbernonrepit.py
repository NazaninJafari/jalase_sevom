import random

list=[]
n = int(input("tool arayeh: "))

for i in range (n) :
    x = random.randint(1,100)
    if x in list :
        print("adad tekrari!! ")

    else :
        list.append(x)    

print(list)        