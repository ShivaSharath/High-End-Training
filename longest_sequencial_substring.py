a=input()
'''b=[]
j=0
for i in range(len(a)-1):
    if ord(a[i+1])==ord(a[i])+1:
        b[j]=b[j]+1
    else:
        j+=1
        continue
x=len(b)
b.sort()
print(b[x-1])'''

c=1
m=0
for i in range(len(a)-1):
    if(ord(a[i])==ord(a[i+1])-1):
        c=c+1
    else:
        if c>m:
            m=c
        c=1
if c>m:
    m=c
print(m)
