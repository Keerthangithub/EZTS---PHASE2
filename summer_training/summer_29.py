'''nums=[13,9,4,10,5,7]
k=[]
for i in range(len(nums)):
    for j in range(i+2,len(nums)):
        if j!=len(nums)-1 or j!=len(nums)-2:
            k.append(nums[i]+nums[j]+nums[j+2])
        else:
            break
print(max(k))
print(k)

def recur(i,i+1)'''
nums = [1,2,2,3,1,4]
c=0
d={}
for i in nums:
     if i in d:
         d[i]=d[i]+1
     else:
         d[i]=1

print(d[3])
