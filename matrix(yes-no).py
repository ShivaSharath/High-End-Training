a=[]
n=int(input())
for i in range(n):
    a.append(input())
b=input()
flag=0
for i in range(len(b)):
    if b[i] not in a[i%n]:
        print('No')
        flag=1
        break
if flag==0:
    print("yes")