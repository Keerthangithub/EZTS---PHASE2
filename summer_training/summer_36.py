'''st="1C0C1C1A0B1"
c,d,e=0,0,0
for i in range(len(st)-1):
    for j in range(d,d+3):
        c=3
        if st[c+1]=='A':
            d=int(st[c])&&int(st[c+2])
        if st[c+1]=='B':
            d=int(st[c])||int(st[c+2])
        if st[c+1]=='C':
            d=int(st[c])^int(st[c+2])
st="1A1B1C1A0C1B1C0A1B0C1"
d=0
i,j,k,m=0,1,2,0
while(m<=len(st)):
    if j<=len(st)-1:
        if st[j]=='A':
            if m==0:
                d=int(st[i])&int(st[k])
                i=d
                j+=2
                k+=2
            else:
                d=i&int(st[k])
                i=d
                j+=2
                k+=2
        elif st[j]=='B':
            if m==0:
                d=int(st[i])|int(st[k])
                i=d
                j+=2
                k+=2
            else:
                d=i&int(st[k])
                i=d
                j+=2
                k+=2
        else:
            if m==0:
                d=int(st[i])^int(st[k])
                #print(d)
                i=d
                j+=2
                k+=2
            else:
                d=i&int(st[k])
                i=d
                j+=2
                k+=2
    m+=1
print(i)'''

s='1C0C1C1A0B1'
res=int(s[0])
i=1
while i <len(s):
    op=s[i]
    val=int(s[i+1])
    if op =='A':
        res=res & val
    elif op =='B':
        res=res | val
    else:
        res=res^val
    i+=2
print(res)

        
        
        