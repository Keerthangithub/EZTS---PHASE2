a=[[1,3],[2,5],[4,6],[6,7],[5,8],[7,9]]
b=[5,6,5,4,11,2]
v=b.copy()
for i in range(1,len(a)):
    for j in range(0,i):
        if a[j][1]<=a[i][0] and v[i]<v[j]+b[i]:
            v[i]=v[j]+b[i]
            
print(v)
