def bubble_sort(a,n):
  cnt = 0
#  print(a)
  flag = 1
  while flag:
    flag = 0
    for j in range(n-1,0,-1):
#      print(a[j],a[j-1])
      if(a[j] < a[j-1]):
        a[j],a[j-1] = a[j-1],a[j]
#        print("change")
        cnt += 1
        flag = 1
  return a,cnt
n = int(input())
a = list(map(int,input().split()))
taple=bubble_sort(a,n)
print(*taple[0])
print(taple[1])
