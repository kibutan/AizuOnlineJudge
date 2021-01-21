n = int(input())

bfrv = [list(map(int,input().split())) for _ in range(n)] 

house1 = [[0]*10 for _ in range(3)]
house2 = [[0]*10 for _ in range(3)]
house3 = [[0]*10 for _ in range(3)]
house4 = [[0]*10 for _ in range(3)]

for j in range(n):
  b = bfrv[j][0]
  f = bfrv[j][1]
  r = bfrv[j][2]
  v = bfrv[j][3]
  if(b == 1):
    house1[f-1][r-1] += v
  if(b == 2):
    house2[f-1][r-1] += v
  if(b == 3):
    house3[f-1][r-1] += v
  if(b == 4):
    house4[f-1][r-1] += v
  
for i in range(0,3):
  print("",*house1[i])
print("####################")
for i in range(0,3):
  print("",*house2[i])
print("####################")
for i in range(0,3):
  print("",*house3[i])
print("####################")
for i in range(0,3):
  print("",*house4[i])
  
