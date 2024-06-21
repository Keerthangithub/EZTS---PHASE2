a=int(input())
for i in range(a):
    for j in range(a):
        if i==0 or i==a-1:
            print("*"*5)
            break
        else:
            if j==0 or j==a-1:
                print("*",end="")
            else:
                k=3
                for i in range(1,k+1):
                        print(i,end="")
