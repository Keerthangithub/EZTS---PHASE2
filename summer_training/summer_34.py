def hi(d):
    s=[]
    s.append(d[0])
    s.append(d[1])
    s.sort()
    print(s,"hi")
l=[4,9,8,2,14,3,5,6]
k=[]
for i in range(len(l)-1):
    k=l[i:i+3]
    print(k)
    hi(k)
print(k)
    