a=list(map(float,input().split(" ")))
e=0
o=0
d=0
for i in range(len(a)):
    if(a[i]%2==0):
        e=e+1
    elif(a[i]%2!=0 and a[i]%1==0):
        o=o+1
    else:
        d=d+1
print(e)
print(o)
print(d)
        