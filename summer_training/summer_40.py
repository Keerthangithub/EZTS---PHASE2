def bfs(d,n):
    v=[]
    q=[n]
    while(q):
        for i in d[q[0]]:
            if i not in q and i not in v:
                q.append(i)
        v.append(q.pop(0))
        print(v[-1])

d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
bfs(d,next(iter(d)))
g={5:[(3,1),(1,2),(6,3)],1:[(5,2),(2,1)],3:[(5,1),(6,3)]}