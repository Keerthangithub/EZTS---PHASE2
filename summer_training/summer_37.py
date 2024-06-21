'''arr=[3,2,1,7,5,4,2,3,6]
arr.sort()
print(arr[-3]+arr[-4])'''
n=12
num=718
d={}
k=65
for i in range(10):
    if i in d:
        d[i]+=1
    else:
        d[i]=i
for i in range(10,36):
    if i not in d:
        d[i]=chr(k)
        k+=1
    else:
        d[i]=k
print(d)
q=float('inf')
r=0
while q!=0:
    r=num%n
    s.append(d[i])