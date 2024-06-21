graph={0:[(1,2)],
       1:[(0,2),(3,3),(2,4)],
       2:[(1,4)],
       3:[(2,3)]}
def dijkstras(start,n):
    visited=set()
    queue=[(start,0)]
    distance=[float('inf')]*(n)
    distance[start]=0
    visited.add(start)
    while queue:
        node,cost=queue.pop(0)
        for i in graph[node]:
            if i[0] not in visited:
                distance[i[0]]=min(distance[i[0]],cost+i[1])
                queue.append((i[0],distance[i[0]]))
                visited.add(i[0])
    print(distance)
dijkstras(0,4)
'''

g={5:[(3,1),(1,2),(6,3)],
   1:[(5,2),(2,1)],
   3:[(5,1),(6,3)]}
def dj(x):
    d={5:999,1:9999,3:9999,6:9999,2:9999}
    d[x]=0
    vi=[]
    q=[x]
    while(q):
        x=q[0]
        for i in g[x]:
            if(i[0] not in vi):
                if(d[i[0]]>i[1]+d[x]):
                    d[i[0]]=i[1]+d[x]
        vi.append(q.pop(0))
    return vi
print(dj(5))'''
