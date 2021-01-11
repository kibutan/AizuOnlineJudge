from collections import deque
n,q = list(map(int,input().split()))
current_time = 0
process = deque([list(map(str,input().split())) for _ in range (n)])
#print(process[0][0])
#for i in range(2):
#  print("i",i)
while process != deque([]):
#  print("before:",process)
#  print("remain time of task:", int(process[0][1]))
  if(int(process[0][1]) <= q):
#    print("less q")
    current_time = current_time + int(process[0][1])
    print(process[0][0],current_time)
    process.popleft()
  else:
#    print("more q")
    current_time = current_time + q
    process.append([process[0][0],str(int(process[0][1])-q)])
    process.popleft()
#  print("after:",process)
#  print(current_time)
