'''def fun(y):
    if y%2!=0:
        return y
    else:
        return

def rec(a,b):
    f=0
    g,h=0,0
    if a[i]%2==0 and b[j]%2!=0:
        f=a[i]+b[j]
        fun(b[g+1:len(b)])'''
        
a=[6,3,2,9,4,7]
b=[8,7,5,3,6,9]
i,j,k=0,0,0
d=[]
v=[]
c=0
while i<len(a):
    if a[i]%2==0:
        j=0
        if c>=1:
            v.append(sum(d)-sum(v))
        while j<len(b):
            k=0
            if b[j]%2!=0:
                k=a[i]+b[j]
                d.append(k)
            j+=1
            c=1
    i+=1
v.append(sum(d)-sum(v))
print(d)
print(v)