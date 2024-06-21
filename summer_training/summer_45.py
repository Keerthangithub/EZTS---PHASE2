nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
nums1.extend(nums2)
nums1.sort()
print(nums1)
for i in range(len(nums1)):
    if i==0:
        nums1.remove(i)
        print(nums1)
print(nums1)
