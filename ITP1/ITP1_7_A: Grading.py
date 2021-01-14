import sys
for i in sys.stdin.readlines():
  m,f,r = map(int,i.split())
  if(m == -1 and f == -1 and r == -1): exit()
  elif(m == -1 or f == -1):print("F")
  elif(m + f < 30):print("F")
  elif(30 <= m + f < 50 and r >= 50):print("C")
  elif(30 <= m + f < 50 and r < 50):print("D")
  elif(50 <= m + f < 65):print("C")
  elif(65 <= m + f < 80):print("B")  
  elif(80 <= m + f):print("A") 
