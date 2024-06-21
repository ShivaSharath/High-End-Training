n=int(input())
m=[]
for i in range(n):
    m.append(list(map(str,input().split())))
w=input()
print(m)

def fun(i,j,k):
    if k==len(w):
        return 1
    if i<0 or j<0 or i>=n or j>=n or m[i][j]!=w[k]:
        return
    t=fun(i+1,j,k+1)
    t=fun(i-1,j,k+1)
    t=fun(i,j+1,k+1)
    t=fun(i,j-1,k+1)
    return t
for i in range(n):
    for j in range(n):
        if m[i][j]==w[0]:
            c=fun(i,j,1,0)
            print("yes")
            break    
if c==0:
    print("no")