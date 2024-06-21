arr=[6700,8858,8858,8858,8858]
k=[]
d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i,j in d.items():
    k.append(j)
for i in d:
    if d[i]==max(k):
        print(i)
        break
print(d)
