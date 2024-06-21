a=list(map(str,input().split(" ")))
k,s,d=0,0,0
for i in range(len(a)):
    if '.' in a[i]:
        k+=float(a[i])
    else:
        if int(a[i])%2==0:
            s+=int(a[i])
        else:
            d+=int(a[i])
print(k)
print(s)
print(d)