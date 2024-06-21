'''k=input()
d=int(input())
s=[]
for i in range(d):
    f=list(map(str,input().split()))
    if f[0]=='L':
        for i in range(int(f[1])):
            
print(f)'''
def Prime_Number(n, i=2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    return Prime_Number(n, i + 1)


n = 971
if Prime_Number(n):
    print("Yes,", n, "is Prime")
else:
    print("No,", n, "is not a Prime")