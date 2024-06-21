a=list(map(int,input().split()))
b=a[0]
pr=0
for i in range(1,len(a)):
    if a[i]<b:
        b=a[i]
    if a[i]>b:
        pr=b-a[i]
print(pr)     
'''d=len(a)-1
s=[]
i,j=0,len(a)-1
while i<=len(a):
    if max(a)==a[i]:
        i=i+1
    if min(a)==a[d]:
        j=j-1
    for x in range(i,j+1):
        s.append(x)
    break
if((max(s)-min(s))>0):
    print(max(s)-min(s))
else:
    print('0')'''
    