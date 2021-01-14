import sys
ans = 0
for i in sys.stdin.readlines():
  n,x = map(int,i.split())
  if(n == 0 and x == 0): 
    exit()
  for j in range(1,n-1):
    for k in range(j+1, n):
      for l in range(k + 1,n+1):
        if(j+k+l == x):ans += 1
  print(ans)
  ans = 0
