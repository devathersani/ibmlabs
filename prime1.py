flag=0
num=int(input("enter number:"))
print(2)
for i in range(1,num+1):
    for j in range(2,i):
        if(i%j == 0):
            flag=0
            break
        else:
            flag=1
    if(flag == 1):
        print(i)