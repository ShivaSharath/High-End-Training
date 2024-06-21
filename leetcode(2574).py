nums=[4,7,5,2,3]
s=sum(nums)
x=0
j=0
for i in nums:
    nums[j]=abs((x)-(s-i-x))
    x=x+i
    j=j+1
print(nums)