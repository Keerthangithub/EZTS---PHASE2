def Prime_Number(n, k):
    if n == k:
        return True
    elif n % k == 0:
        return False
    return Prime_Number(n, k + 1)

def sep(num):
    c,d,e=0,0,0
    for i in range(2,num):
        for j in range(2,num):
            if i+j==num:
                c,d=i,j
                e=1
            if e==1:
                if Prime_Number(c,2):
                    if Prime_Number(d,2):
                        return c,d
                    else:
                        continue
                else:
                    continue
num=10
c,d=sep(num)
print(c)
print(d)

    