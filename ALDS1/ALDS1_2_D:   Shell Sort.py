def inserionSort(a,n,g,cnt):
  for i in range(g,n):
    v = a[i]
    j = i - g
    while j >= 0 and a[j] > v:
#      print("cnt:",cnt)
#      print("a[j+g]:",a[j+g]," a[j]:",a[j])
      a[j+g] = a[j]
      cnt += 1
#      print("cnt:",cnt)
      j -= g
    a[j+g] = v
#    print("insert:",a)
  return cnt,a

def shell_sort(a,n):
  cnt = 0
  k = 4
  g = [1]
  while k < n :
    g.insert(0,k)
#    print("g",g)
    k = k*3+1
#  print(k)
  m = len(g)
  for i in range(m):
    insert = inserionSort(a,n,g[i],cnt)
    cnt = insert[0]
#    print("insert_cnt",insert[0])
#  print("shell:",a)
  return m,g,insert[0],a

n = int(input())
a = [int(input()) for _ in range(n)]
shell = shell_sort(a,n)
print(shell[0])
print(*shell[1])
print(shell[2])
for _ in range(len(shell[3])):
  print(shell[3][_])
