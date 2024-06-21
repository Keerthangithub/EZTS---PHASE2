def is_prime(k):
    c=0
    for i in range(1,k+1):
        if k%i==0:
            c+=1
    if c==2:
        return k
    else:
        return -1
def prime(a):
    s,k,d=0,0,0
    for i in str(a):        #s=0
        s+=int(i)           #while(n)
    for i in str(s):        #s=s+(n%10)
        k+=int(i)           #n=n//10
    d=is_prime(k)
    if d==-1:
        return prime(a+1)
    else:
        return a
a=int(input())
print(prime(a))
