x=input()
d=[]
c=0
s=set()
for i in x:
    s.add(i)
for i in s:
    for j in range(len(x)):
        if i==x[j]:
            c+=1
        else:
            d.append(c)
            c=0
print(s)
'''for i in range(len(x)):
    i=i+k[i-1]
    d=ord(x[i])
    for j in range(len(x)):
        if d==ord(x[j]):
            c+=1
        else:
            k.append(c)
            c=0
            break
        
print(k)'''