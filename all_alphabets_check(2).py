'''s="abfgresagtyuiofde"
c=0
for i in range(len(s)):
    substring=''
    for j in s[i:]:
        if j not in substring:
            substring=substring+j
        else:
            c=max(c,len(substring))
print(c)'''

s = input()
sub = ''
length = max_len = i = 0
while i<len(s):
    if s[i] not in sub:
        sub += s[i]
        length += 1
        i += 1
        
    else:
        max_len = max(length, max_len)
        length -= sub.index(s[i])+1
        sub = sub[sub.index(s[i])+1:]

max_len = max(length, max_len)
print(max_len)