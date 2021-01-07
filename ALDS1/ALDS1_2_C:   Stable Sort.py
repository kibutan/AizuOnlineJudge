def bubble_sort(c,n):
  for i in range(n):
    for j in range(n-1, i,-1):
      if(c[j][1] < c[j-1][1]):
        c[j],c[j-1] = c[j-1],c[j]
  return c
def select_sort(c,n):
  for i in range(n):
    minj = i
    for j in range(i,n):
      if(c[j][1] < c[minj][1]):
        minj = j
    c[i],c[minj] = c[minj],c[i]
  return c
n = int(input())
c = list(map(str,input().split()))
c_copy=c[:]
print(*bubble_sort(c_copy,n))
print("Stable")
print(*select_sort(c,n))
stability = ( c == c_copy)
#print(stability)
if(stability):print("Stable")
else:print("Not stable")
