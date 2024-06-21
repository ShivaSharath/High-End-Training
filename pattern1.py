a=int(input())
r=1
m=[]
for i in range(a):
    for j in range(a):
        if i==0 or i==(a-1) or j==0 or j==(a-1):
            print("*",end='')
        else:
            print(r,end='')
            r+=1
    print()
    