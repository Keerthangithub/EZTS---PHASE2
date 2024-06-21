'''for i in range(1,a+1):
    if a%i==0:
        c+=1
if(c<=2):
    print(a)'''
def rec(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if(c==2):
        return a
    else:
        return rec(a+1)
a=int(input())
print(rec(a))
