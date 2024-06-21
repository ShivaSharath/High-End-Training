def isprime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1
def lprime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0
a=list(map(int,input().split(" ")))
s=0
for i in range(len(a)-1):
    s=s+lprime(a[i],a[i+1])
print(s)


'''
l=list(map(int,input().split(",")))
maxx=0
for i in range(len(l)-1):
    j=l[i]
    k=l[i+1]
    for a in range(j,k):
        for b in range(2,(a//2)+1):
            max=0
            if a%b==0:
                if max<a:
                    max=a
        print(max)
    maxx+=max
print(maxx)
'''