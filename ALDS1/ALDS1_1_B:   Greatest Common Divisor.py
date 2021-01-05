import math
x, y = list(map(int,input().split()))
#print(math.gcd(x,y))
tmp = 0
while y != 0:
  tmp = x
  x = y
  y = tmp%y
print(x)
