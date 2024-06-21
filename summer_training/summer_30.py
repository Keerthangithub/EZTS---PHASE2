l=input()
d={}
for i in l:
    if i not in d and i!=" " and (i>='a' and i<='z'):
        d[i]=1
c=0
for i in d:
    c+=d[i]
print(c)
print(d)
if c==26:
    print(True)
else:
    print(False)