l=input()
n=int(input())
m=[input() for i in range(n)]
b=[]
def bc(l, a, i):
    if len(a) == 3 and a not in b:
        b.append(a[:])  
        return
    for j in range(i, len(m)):
        a.append(m[j])
        bc(m, a, j + 1)
        a.pop() 


x=''
bc(l,[],0)
for i in m:
    a=i.split(" ")
    if a[0]=="m" or a[0]=='r':
        x+=[int(a[1])]
print(b)    
print(x)
f=0
for i in b:
    f=0
    for j in x:
        if j not in i:
            f=1
            break
    if f==0:
       print("yes")
       break
else:
    print("no")
        
    

# print(b)




'''
a=input()
n=int(input())
str=''
for i in range(n):
    b=input()
    if(b[0]=='L'):
        str.append(a[int(b[2])])
    else:
        str.append(a[-int(b[2])])
str.sort()
b=[]
for i in range(len(a)-n+1):
    t=list(a[i:n+1])
    t.sort()
    b.append(t)
print(b)
print(str)
for i in b:
    if i==str:
        print("yes")
        break
    else:
        print("no")'''
        
