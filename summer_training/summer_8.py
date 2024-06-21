a=str(input())
c=0
for i in range(len(a)):
    c=0
    for j in range(1,int(a[i])+1):
        if int(a[i])%j==0:
            c+=1
    if c==2:
        print(int(a[i]))
    