s="cc"
c,d=1,0
k=[]
if len(s)==1:
    print(1)
else:
    for i in range(len(s)-1):
        if ord(s[i])==ord(s[i+1]):
            d=0
        if ord(s[i])!=ord(s[i+1]):
            d,c=1,1
        if d==0:
            c+=1
            k.append(c)
        '''else:
            k.append(c)
            print(k)
            c=1'''
    print(max(k))
    print(k)
'''nums=[4,3,2,1]
k=[]
d=0
for i in range(len(nums)):
    if i%10==nums[i]:
        k.append(i)
print(min(k))
1636
1394
1446
162
496
2053
2040'''
