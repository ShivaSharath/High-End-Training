l=list(map(int,input().split(",")))
j=1
k=2
for i in range(len(l)-2):
    if l[i]<l[j]:
        l[j],l[i]=l[i],l[j]
    if l[j]<l[k]:
        l[j],l[k]=l[k],l[j]
    if l[k]<l[i]:
        l[i],l[k]=l[k],l[i]
    j+=1
    k+=1
print(l)

'''
            METHOD-1
--------------------------------------------
    if l[k]<l[j]:
        l[j],l[k]=l[k],l[j]
    if l[j]<l[i]:
        l[i],l[j]=l[j],l[i]


            METHOD-2
--------------------------------------------
for i in range(len(l)-2):
    if l[i]<l[i+1]:
        l[i+1],l[i]=l[i],l[i+1]
    if l[i+1]<l[i+2]:
        l[i+1],l[i+2]=l[i+2],l[i+1]
    if l[i+2]<l[i]:
        l[i],l[i+2]=l[i+2],l[i]
    '''
