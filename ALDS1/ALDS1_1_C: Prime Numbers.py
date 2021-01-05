import math
def prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if(n % i == 0):return False
  return True
n = int(input())
a = [int(input()) for _ in range(n)]
cnt = 0
for j in range(n):
  if(prime(a[j])):cnt +=1
print(cnt)
