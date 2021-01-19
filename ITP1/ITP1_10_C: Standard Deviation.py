import sys
import statistics
s = []
s_int = []
for i in sys.stdin.readlines():
  s.append(i.split())
for j in range(0,len(s),2):
#  print("j",j)
  if(s[j] == ['0']):
#    print("exit")
    exit()
  else:
    s_int = [int(_) for _ in s[j+1]]
#    print("s[j]",s[j+1])
#    print(s_int)
    print(statistics.pstdev(s_int))
