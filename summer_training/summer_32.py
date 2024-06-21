arr = [1,2,3,5]
k = 3
s=[]
'''786
d=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        s.append(arr[i]/arr[j])
s.sort()
d=s[k-1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if d==arr[i]/arr[j]:
            print(i,j)
            break
print(s)
print(d)
print(2/5)'''
s="Hello world"
d=list(list(s))
print(list(d))
1417

