a=list(map(str,input().split(",")))
d=0
for i in a:
    c,k=0,[]
    for j in range(len(i)):
        if i[j]!=":":
            if i[j] in 'abcdefghijklmnopqrstuvwxyz':
                c+=1
            if i[j] not in 'abcdefghijklmnopqrstuvwxyz' and i[j] in '0123456789' and i[j]!=':':
                if str(c)==i[j]:
                    print(i[c-1])
                    break
                
            
                    
        if i[j]==':':
            continue
