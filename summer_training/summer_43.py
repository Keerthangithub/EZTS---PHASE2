a=[[1,3],[2,5],[4,6],[6,7],[5,8],[7,9]]
b=[5,6,3,4,11,2]
k,c=0,0
d=[]
v=[]
for g in range(len(b)-1):
    for i in range(len(b)-1):
        if b[i]==max(b):
            k=i
            d.append(b[i])
            v.append(a[i])
            b.remove(max(b))
            c=1
            break
        if c==1:
            if b[i]==max(b):
                for j in range(len(a[i])):
                    if a[j][j+1]<=v[j][j]:
                        v.append(a[i])
                        d.append(b[i])
                        b.remove(max(b))
                        break
                    else:
                        break
        else:
            continue
s=[]
for i in v:
    if i not in s:
        s.append(i)
print(s)
#print(v)
print(d[0:len(s)])
