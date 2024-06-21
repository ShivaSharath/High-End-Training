a=[1,5,8,9]
b=[2,7,9,10,14]
c=[]
i=0
j=0
while len(a)>i and len(b)>j:
    if a[1]<b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1
if(j<len(b)):
    c.extend(b[j:])
if(j<len(a)):
    c.extend(a[j:])
print(c)