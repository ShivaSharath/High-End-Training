s="abfgresagtyuiofde"

c=0
for i in range(len(s)):
    substring=''
    for j in s[i:]:
        if j not in substring:
            substring=substring+j
        else:
            c=max(c,len(substring))
print(c)
