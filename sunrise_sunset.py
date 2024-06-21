a=[3,5,9,6,8,10]
ma=0
r=[]
for i in range(len(a)):
    if ma<a[i]:
        ma=a[i]
        r.append(a[i])
print(r)
a1=a[::-1]
ma=0
r=[]
for i in range(len(a1)):
    if ma<a1[i]:
        ma=a1[i]
        r.append(a1[i])
print(r)