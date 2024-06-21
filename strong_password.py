a=list(map(str,input()))
l,u,d,s,r=0,0,0,0,0 
for i in range(0,len(a)):
    if(a[i] in [1,2,3,4,5,6,7,8,9,0]):
        d=d+1
    elif(a[i].isupper()):
        u=u+1
    elif(a[i].islower()):
        l=l+1
    else:
        s=s+1
if(l==0):
    r=r+1
if(u==0):
    r=r+1
if(d==0):
    r=r+1
if(s==0):
    r=r+1
if(r<(8-len(a))):
    r+=(8-len(a))-r
    print(r)
if(l>0 and u>0 and d>0 and s>0 and c>0):
    print('-1')

    