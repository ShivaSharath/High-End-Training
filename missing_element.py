n=7
l=[0,5,3,6,7,2,1]
l.sort()
c=0
for i in l:
    if i==c:
        c=c+1
    else:
        print(c)