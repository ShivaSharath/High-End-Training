s=input()
c1=0
c2=0
for i in s:
    if i=='M':
        c1=c1+1
    elif i=='N':
        c2=c2+1
if c1==c2:
    print(0)
elif c1>c2:
    print('M')
else:
    print('N')