s = input()
n = int(input())
c = [list(map(str,input().split())) for _ in range(n)]

def print_(s,a,b):
  return s[a:b+1]

def reverse_(s,a,b):
  s_rev = s[a:b+1]
  s_rev = s_rev[::-1]
#  print("rev",s_rev)
#  print(":a",s[:a])
#  print("a:b",s_rev[a:b+1])
#  print("b+1:",s[b+1:])
  s = s[:a] + s_rev + s[b+1:]
  return s

def replace_(s,a,b,str):
  s =s[:a] + str + s[b+1:]
  return s

for i in range(n):
#  print("before",s)
  if(c[i][0] == "replace"):s = replace_(s,int(c[i][1]),int(c[i][2]),c[i][3])
  elif(c[i][0] == "reverse"):s = reverse_(s,int(c[i][1]),int(c[i][2]))
  elif(c[i][0] == "print"):print(print_(s,int(c[i][1]),int(c[i][2])))
#  print("after",s)
#  print("i",i)    
