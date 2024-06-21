l=[1,8,3,1,1,1,2,1,1,3]
p1=1
p=l[0]
for i in range(1,len(l)):
    if l[i]==p:
        p1=p1+1
    else:
        if p1!=0:
            p1=p1-1
        if p1==0:
            p1=p1+1
            p=l[i]
print(p)