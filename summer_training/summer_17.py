s,x=0,0
k=len(nums)
k.append(s)
d.append(x)
for i in range(len(nums)):
    if len(nums)==(k+k):
        break
    s+=nums[i]
    nums.append(s)
for i in range(1,k):
    if len(nums)==K*3:
        break
    x+=nums[-i]
    nums.append(x)
for i in range(k):
    nums.pop(i)
for i in range(k):
    for j in range(len(nums),k,-1):
        nums.append(abs(nums[i]-nums[j]))
return nums
