a=list(map(int,input().split()))
m1=0            
for i in range(len(a)-1):
    for j in range(i+1,len(a)):      #if(a[i]<a[j] and a[j]-a[i] >m1):
        x=a[j]-a[i]                         #m=a[j]-a[i]
        if(m1<x):                           #
            m1=x                            #
print(m1)