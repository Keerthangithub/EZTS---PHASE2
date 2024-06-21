l=[4,8,2,4,4,8,4]
d={}
for i in l:
    if i not in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            c+=1
    if l[i] not in k:
        k.append(c)
for i in k:
    if i>len(l)//2:'''
        
    