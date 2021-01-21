class dice:
  top=s=e=w=n=bottom = 0
  def __init__(self,_1,_2,_3,_4,_5,_6):
    self.top = _1
    self.s =_2
    self.e = _3
    self.w = _4
    self.n = _5
    self.bottom = _6
  def test_dice(self):
    print("top",self.top, "south",self.s, "east",self.e, "west",self.w, "north",self.n, "bottom",self.bottom)
  def roll(self,direction):
    if(direction == "N"):
      self.top,self.s,self.n,self.bottom = self.s,self.bottom,self.top,self.n
    if(direction == "E"):
      self.top,self.e,self.w,self.bottom = self.w,self.top,self.bottom,self.e
    if(direction == "W"):
      self.top,self.e,self.w,self.bottom = self.e,self.bottom,self.top,self.w
    if(direction == "S"):
      self.top,self.s,self.n,self.bottom = self.n,self.top,self.bottom,self.s
  def ans_1(self):
    print(self.top)
  def ans_2(self,t,f):
      if(self.s == f):print(self.e)
      elif(self.e == f):print(self.n)
      elif(self.w == f):print(self.s)
      elif(self.n == f):print(self.w)
      else:print(self.top,f)
#      self.test_dice()
    
    
##ans_1
##top,s,e,w,n,bottom = list(map(int,input().split()))
##direction = input()
##

##ans2
top,s,e,w,n,bottom = list(map(int,input().split()))
q = int(input())
#t,f = [list(map(int,input().split())) for _ in range(n)]  -> move to under
##

##dice make
dice1 = dice(top,s,e,w,n,bottom)
#dice1.test_dice()
##

#################ans_1
#for i in range(len(direction)):
#  dice1.roll(direction[i])
#  dice1.test_dice()
#dice1.ans_1()
######################

##################ans2
for i in range(q):
  t,f = list(map(int,input().split()))
#  print(dice1.test_dice())
  if(t == dice1.top):
#    print("t == top")
    dice1.ans_2(dice1.top,f)
  elif(t == dice1.s):
#    print("t == s")
    dice1.roll("N")
    dice1.ans_2(dice1.top,f)
  elif(t == dice1.e):
#    print("t == e")
    dice1.roll("W")
    dice1.ans_2(dice1.top,f)
  elif(t == dice1.w):
#    print("t == w")
    dice1.roll("E")
    dice1.ans_2(dice1.top,f)
  elif(t == dice1.n):
#    print("t == n")
    dice1.roll("S")
    dice1.ans_2(dice1.top,f)
  else:
#    print("t ==b")
    dice1.roll("S")
    dice1.roll("S")
    dice1.ans_2(dice1.top,f)

  
