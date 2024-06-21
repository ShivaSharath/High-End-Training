"""def pal(a,i):
    r=a%10
    a=a//10
    s=s+(r*(pow(10,i)))
    if a>0:
        pal(a,i+1)
    return s
a=int(input())
i=0
print(pal(a,i))"""

def pal(a,re):
    if(a==0):
        return re
    re=re*10+(a%10)
    return pal(a//10,re)
a=int(input())
if(a==pal(a,0)):
    print("Palindrome")
else:
    print("Not Palindrome")
    