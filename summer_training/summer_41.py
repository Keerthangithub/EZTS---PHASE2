def dijkstras(g,x):
    d={5:9999,1:9999,3:9999,6:9999,2:9999}
    d[x]=0
    v=[]
    q=[x]
    while q:
        x=q[0]
        for i in g[x]:
            if i[0] not in v:
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        v.append(q.pop(0))
    print(v)
    
g={
    5:[(3,1),(1,2),(6,3)],
    1:[(5,2),(2,1)],
    3:[(5,1),(6,3)]
}
dijkstras(g,1)