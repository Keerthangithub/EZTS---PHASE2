nums=[1,2,3,2]
c=0
for i in range(len(nums)):
    if nums.count(i)==1:
        c+=nums[i]
print(c)
