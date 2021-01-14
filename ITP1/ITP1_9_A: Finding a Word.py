import sys
s = input().lower()
p = []

for i in sys.stdin.readlines():
  p.append(i.lower().split())
#print(p)
sum = 0
for i in range(len(p)):
#  print(p[i].count(s))
  sum += p[i].count(s)
print(sum)
