r,c = list(map(int,input().split()))
array = [list(map(int,input().split())) for _ in range(r)]
for i in range(r):
  array[i].append(sum(array[i][:]))
  print(*array[i])
total = 0
arr_total = 0

for j in range(c):
#  print("j",j)
  for k in range(r):
#    print("k",k)
#    print(array[k][j])
    total += array[k][j]
    arr_total += array[k][j]
#  print("total",total,end = "")
#  print("arr_total",arr_total)
  print(total,end = " ")
  total = 0
print(arr_total)
