a=input()
b=int(input())
'''c='abcdefghijklmnopqrstuvwxyz'
for i in a:
    if i in c: 
        p=c.find(i)
        h'''
c=b%26
for i in a:
    if((ord(i)-c)>=97):
        print(chr(ord(i)-c))
    else:
        print(chr(ord(i)-c+26))
    
    
    
    