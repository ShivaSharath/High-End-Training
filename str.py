a="aaabbbaaaaddd"
b=""
i=0
count=1
for i in range(len(a)-1):
    if(a[i]==a[i+1]):
        count+=1
    else:
        b=b+a[i]
print(b)

