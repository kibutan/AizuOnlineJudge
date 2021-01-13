#行数不明の入力を受け取る
# a,b のスワップをちょっとa,bの大小関係に基づいて買える(ワンライナーで)

import sys
for i in sys.stdin.readlines():
  a,b = map(int,i.split())
  a,b = min(b,a),max(b,a)
  if(a == 0 and b ==0): exit()
  print(a,end = " ")
  print(b)
