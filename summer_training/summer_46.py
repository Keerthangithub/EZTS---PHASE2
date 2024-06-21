'''def recur(d,i,s,c):
    if i<=len(d):
        while s>d[i]:
            s=s-d[i]
            c+=1
        i+=1
    return recur(d,i,s,c)'''
a=[1,2,4,5]
a.sort(reverse=True)
k=int(input())
s=k
if k%2!=0 and k>=a[-1]:
    print(k//a[-1])
else:
    c=0
    while(1):
        d=max(a)
        while s>d:
            s=s-d
            c+=1
        a.remove(max(a))
        if a==[]:
            break
    print(c)
            
                
                
            
            
