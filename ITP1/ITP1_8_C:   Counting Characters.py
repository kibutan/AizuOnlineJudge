import sys
s = ""
for i in sys.stdin.readlines():
  s += i.lower()
for j in range(ord("a"),ord("z")+1):
  print(chr(j),":", s.count(chr(j)))
