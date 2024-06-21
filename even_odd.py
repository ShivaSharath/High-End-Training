def out(a,b):
    for i in a:
        if i%2==0:
            e+=i
    for i in b:
        if i%2!=0:
            o+=i
    return e,o
a=[2,3,7,9,5]
b=[1,4,6,8]
c,d=out(a,b)
print(c,d)