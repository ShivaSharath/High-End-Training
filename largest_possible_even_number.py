u='tu5g2k1h8'
v='g5g8gd6h3'
n=[]
for i in u:
    if i.isdigit() and i not in n:
        n.append(i)
for i in v:
    if i.isdigit() and i not in n:
        n.append(i)
n.sort(reverse=True)
if int(n[-1])%2!=0:
    n1=n[::-1]
    for i in range(1,len(n1)):
        if int(n1[i])%2==0:
            n1[i],n1[0]=n1[0],n1[i]
            break
    n=n1[::-1]
n=int("".join(i for i in n))
print(n)