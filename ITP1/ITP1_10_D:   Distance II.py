import math
n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
distance_1 = 0
distance_2 = 0
distance_3 = 0
distance_inf = 0
for i in range(n):
  distance_1 += abs(x[i]-y[i])
  distance_2 += abs(x[i]-y[i]) ** 2
  distance_3 += abs(x[i]-y[i]) ** 3
  distance_inf = max(distance_inf,abs(x[i]-y[i]))
distance_2 = math.sqrt(distance_2)
distance_3 = math.pow(distance_3,1/3)

print(distance_1)
print(distance_2)
print(distance_3)
print(distance_inf)
