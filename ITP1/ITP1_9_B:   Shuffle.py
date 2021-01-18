import sys
p = []
for i in sys.stdin.readlines():
  p.append(i.strip("\n"))
#  print("p in input:",p)
ans=[]
for j in range(len(p)):
  if(p[j] == "-"):exit()
  elif(p[j].isalpha()):
    ans = p[j]
#    print(p[j],"is str")
#    print("ans",ans)
    for k in range(1,int(p[j+1])+1):
      ans = ans[int(p[j+1+k]):]+ans[:int(p[j+1+k])]
#      print(int(p[j+1+k]))
#      print("ans[前半]",ans[int(p[j+1+k]):])
#      print("ans[後半]",ans[:int(p[j+1+k])])  
#      print("k",k)
    print(ans)
    j = int(p[j+1]) + 1
#  elif(p[j].isdecimal()):print(p[j],"is num")
