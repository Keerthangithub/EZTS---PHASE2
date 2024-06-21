s='is2 sentence4 this1 a3'
k=[]
d=[]
o=[]
f=[]
for i in s:
    k.append(i)
for i in k:
    if (i>='a' and i<='z') or (i>='A' and i<='Z'):
        s=0
    else:
        d.append(i)
for i in d:
    if i!=' ':
        o.append(int(i))
for i in o:
    f.append(s[i])
print(f)