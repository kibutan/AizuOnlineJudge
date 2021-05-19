from collections import deque
n = int(input())
ukv=[[0,0,0]]+ [list(map(int,input().split())) for _ in range(n)]
arrive = deque([1])
time = 1
f = [0]*(n+1)
d = [0]*(n+1)
d[1] = time
stack = deque([1])

while(stack):
    s = stack[0]
    k = ukv[s][1]
    if k == 0:
        v = stack.popleft()
        time += 1
        f[v] = time
    else:
        v=ukv[s].pop(2)
        # stack.appendleft(ukv[s][2])
        ukv[s][1] -= 1
        if(v not in arrive):
            stack.appendleft(v)
            arrive.append(v)
            time += 1
            d[v] = time
for i in range(1,n+1):print(i,d[i],f[i])
