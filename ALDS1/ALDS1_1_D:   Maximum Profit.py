n = int(input())
a = [int(input()) for _ in range(n)]
#ans = -1000000000
#tmp = []
#for i in range(n-1):
##  for j in range(i+1,n):
#    tmp.append(a[j])
#    tmp = list(set(tmp))
#  ans = max(ans,(max(tmp)-a[i]))
#  tmp=[]
#print(ans)
min = a[0]
profit = max(a[1:])-a[0] 
for i in range(1,n-1):
  if(min > a[i]):
    min = a[i]
    profit = max(profit,max(a[i+1:]) - a[i])  
print(profit)
