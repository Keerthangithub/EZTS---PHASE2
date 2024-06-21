def fa(x):
    if x==0:
        return 0
    return x+fa(x-2)
a=int(input())
if a%2==0:
    print(fa(a))
else:
    print(fa(a-1))