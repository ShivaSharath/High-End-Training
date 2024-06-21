s=input()
r=[]
for i in s:
    if i!='*':
        r.append(i)
    else:
        r.pop()
print(''.join(r))