a="placements"
s=[]
for i in a:
    if i in 'aeiou':
        s.append(i)
t=list(map(lambda x: x.upper(), s))
print(t)