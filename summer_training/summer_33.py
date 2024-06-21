def prime(a,b):
    k=[]
    for i in range(a,b+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            k.append(i)
        else:
            k.append(0)
    return max(k)

l=[14,16,20,22]
s=[]
for i in range(len(l)-1):
    s.append(prime(l[i],l[i+1]))
print(sum(s))
print(s)

        
    