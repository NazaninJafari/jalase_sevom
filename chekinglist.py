from operator import index


list=[]
b = 1
a = 0
y = 0

n = int(input("toole arayeh: "))

for i in range(n) :
    x = int (input("enter your number: "))
    list.append(x)

while a < n :

    for i in range (n-1) :

        if list[a] < list[b] :
            b += 1
        
        elif list[a] > list[b] :
         
            print ("namoratab")
            y = 1
            break

    a += 1 
    b = a+1
    n -= 1

    if y == 1 :
        break

if y == 0 :
    print("moratab")