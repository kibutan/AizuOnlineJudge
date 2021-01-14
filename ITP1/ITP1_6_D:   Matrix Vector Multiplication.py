import numpy as np
n,m = list(map(int,input().split()))
array = np.array([list(map(int,input().split())) for _ in range(3)])
vector = np.array([int(input()) for j in range(m)])
#print(array)
#print(vector)
ans = np.dot(array,vector)
for i in ans:
  print(i)
