s='leet**cod*e'
b=[]
for i in s:
    if i!='*':
        b.append(i)
    else:
        if b:
            b.pop()
print(''.join(b))