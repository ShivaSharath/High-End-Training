def function(a):
    if(a==1):
        return 1
    return a*function(a-1)
print(function(10))
