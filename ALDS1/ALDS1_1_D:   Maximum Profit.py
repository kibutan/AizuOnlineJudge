n = int(input())
a = [int(input()) for _ in range(n)]
ans = -1000000000
tmp = []
for i in range(n-1):
  for j in range(i+1,n):
    tmp.append(a[j])
    tmp = list(set(tmp))
  ans = max(ans,(max(tmp)-a[i]))
  tmp=[]
print(ans)
