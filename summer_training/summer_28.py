def hi(k):
    d=""
    for i in k[0]:
        if i in k[1]:
            d+=i
    for i in k[1]:
        
            
a=int(input())
k=[]
for i in range(a):
    k.append(input())
print(hi(k))
