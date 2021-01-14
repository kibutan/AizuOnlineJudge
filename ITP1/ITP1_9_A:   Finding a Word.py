import sys,re
s = input().lower()
p = ""

for i in sys.stdin.readlines():
  p += i
#  print(p)
#print(p)
ans = p.lower().count(s)
bad = re.findall("[a-zA-Z0-9][^\n\s]+"+s +"|"+ s+"[a-zA-Z0-9][^\n\s]+",p)
good = re.findall("[\W]+"+s+"|"+s+"[\W]+",p)
all = re.findall(s,p)
print("bad:",len(bad))
print("good:",len(good))
print("all",len(all))
print("bad:",bad)
print("good:",good)
print("all",all)
