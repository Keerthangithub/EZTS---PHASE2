a=int(input())
b=int(input())
c=0
for i in range(a,b):
    if i%7==0:
        c+=1
        print(i,end=",")
print("\n")
print(c)

print(int((a/7)-(b/7)))