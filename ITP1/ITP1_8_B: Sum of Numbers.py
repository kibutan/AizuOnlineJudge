import sys
for i in sys.stdin.readlines():
  a = int(i)
  if(a == 0):exit()
  ans = 0
  for j in range(len(str(a))):
    ans += int(str(a)[j])
  print(ans)
  ans = 0
