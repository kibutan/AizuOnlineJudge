from collections import deque
n = int(input())
ukv = [list(map(int,input().split())) for _ in range(n)]
G = {ukv[i][0]: ukv[i][2:] if ukv[i][1] != 0 else [] for i in range(n)}

score = {x: -1 for x in range(n+1)}
queue = deque()
arrived = []
def bfs(start,cnt = 0):
    queue.append(start)
    score[start] = cnt
    while(len(queue) > 0):
        current = queue.popleft()
        arrived.append(current)
        cnt = score[current]
        for next in G[current]:
            if(next in arrived):continue
            if(next in queue):continue
            queue.append(next)
            score[next] = cnt + 1

bfs(1)
for i in range(1,n+1):
    print(i, score[i])
