n,m = list(map(int,input().split()))
array = [list(map(int,input().split())) for _ in range(n)]
vector = [int(input()) for j in range(m)]

ans = 0
ans_vec = []
for j in range(n):
  for i in range(m):
    ans = ans + (array[j][i] * vector[i])
  ans_vec.append(ans)
  ans = 0

for i in range(len(ans_vec)):
  print(ans_vec[i])
