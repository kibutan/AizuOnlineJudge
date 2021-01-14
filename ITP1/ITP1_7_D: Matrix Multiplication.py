n,m,l = list(map(int,input().split()))
array_A = [list(map(int,input().split())) for _ in range(n)]
array_B = [list(map(int,input().split())) for _ in range(m)]
ans = 0
ans = [[0 for _ in range(l)]for _ in range(n)]
for i in range(n):
  for j in range(m):
    for k in range(l):
#      print("k",i)
#      print("j",j)
#      print("k",k)
      ans[i][k] += (array_A[i][j]*array_B[j][k])
#      print("ans",ans)
  print(*ans[i], end = "")
  print()
#      print("array_A",array_A[i][j])
#      print("array_B",array_B[j][k])
