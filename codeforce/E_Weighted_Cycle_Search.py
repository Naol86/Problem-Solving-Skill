from collections import *
x = int(input())
for i in range(x):
    n,m = [int(i) for i in input().split()]
    lis = []
    for j in range(m):
        u,v,w = [int(i) for i in input().split()]
        lis.append([u,v,w])
    lis.sort(reverse = True, key = lambda x: x[2])
    
    size = n
    root = {i:i for i in range(1,size+1)}
    rank = [0 for i in range(size)]

    def find(x):
        if x == root[x]:
            return x
        root[x] = find(root[x])
        return root[x]
    def union(x,y):
        px = find(x)
        py = find(y)

        if px != py:
            if rank[px-1] < rank[py-1]:
                root[px] = root[py]
            elif rank[px-1] > rank[py-1]:
                root[py] = root[px]
            else:
                root[py] = root[px]
                rank[px-1] +=1
            return False
        return True
    
    graph = defaultdict(list)
    ans = [0,0,float("inf")]
    for u,v,w in lis:
        if union(u,v):
            if ans[2] > w:
                ans = [u,v,w]
        else:
            graph[u].append(v)
            graph[v].append(u)
    # print(ans)
    parent = defaultdict(int)
    queue = deque([ans[0]])
    parent[ans[0]] = -1
    while queue:
        par = queue.popleft()
        if par == ans[1]:
            break
        for node in graph[par]:
            if node in parent:
                continue
            parent[node] = par
            queue.append(node)
    path = []
    na = ans[1]
    while na != -1:
        path.append(na)
        na = parent[na]
    print(ans[2],len(path))
    print(*path)
