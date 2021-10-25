n,q = list(map(int,input().split()))
cxy = [list(map(int,input().split())) for _ in range(q)]
com,x,y = [list(i) for i in zip(*cxy)]
parents = list(range(n))
rank = [0] * n
# class unionfind(self,x,y):
#     def __init__(self):
#         return True

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if rank[x] < rank[y]:
        parents[x] = y
        # rank[x] += 1
    else:
        parents[y] = x
        if rank[x] ==rank[y] :rank[x] += 1
        # while y in parents:parents[parents.index(y)] = x

def find(x):
    if parents[x] == x:return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def same(x,y):
    return find(x) == find(y)

for i in range(q):
    # print(com[i],x[i],y[i])
    if(com[i] == 0):unite(x[i],y[i])
    elif(com[i] == 1):print(int(same(x[i],y[i])))
    # print("parents",parents)
