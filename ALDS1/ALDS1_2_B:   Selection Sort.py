def selection_sort(a,n):
  cnt = 0
  for i in range(n-1):
    minj = i
    for j in range(i, n):
      if(a[j] < a[minj]):
#        print(a[j],a[minj])
        minj = j
        
    a[i],a[minj] = a[minj], a[i]      
#    print(a)
    if(i != minj):cnt += 1
  return a,cnt
n = int(input())
a = list(map(int,input().split()))
taple=selection_sort(a,n)
#print(taple)
print(*taple[0])
print(taple[1])
