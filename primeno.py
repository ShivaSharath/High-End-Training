'''n=int(input())
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 1
    return 0
while True:
    if n%2==0 and n!=2:
        n+=1
    elif prime(n)==0:
        break
    else:
        n+=1
print(n)
    ----------------------------
    ---------------------------- 
question 2
a=735
c1,c2=0,0
while(a>0):
    r=a%10
    for i in range(2,(r//2)+1):
        if(r%i==0):
            c1=c1+1
            break
    if(c1==0):
        c2=c2+1
    a=a/10#
    ------------------------------

a=45678
c=0
while(n):
    if(n%10 in [2,3,5,7]):
        c=c+1
    n=n//10
print(c)'''

        