n = list(map(str,input().split()))
stack = []
ans = 0
for i in range(len(n)):
  stack.append(n[i])
#  print(stack)
#  print("i:",i)
  if(n[i] != "+" and n[i] != "-" and n[i] != "*"):continue
  else:
#    print("operator:",stack)
    if(n[i] == "+"):
      ans = int(stack[-3])+int(stack[-2])
    elif(n[i] == "-"):
      ans = int(stack[-3])-int(stack[-2])
    elif(n[i] == "*"):
      ans = int(stack[-3])*int(stack[-2])
#    print("before pop:",stack)
    stack.pop(-1)
    stack.pop(-1)
    stack.pop(-1)
    stack.append(str(ans))
#    print("pop:",stack)
print(ans)

