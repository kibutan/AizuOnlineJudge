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

##ans3 Global function
def ans_3(dice1,dice2):
  if(dice1.top == dice2.top and dice1.s == dice2.s and dice1.e == dice2.e and dice1.w == dice2.w and dice1.n == dice2.n and dice1.bottom == dice2.bottom): 
    print("Yes")
    exit()
  elif(dice1.top == dice2.top and dice1.s == dice2.e and dice1.e == dice2.n and dice1.w == dice2.s and dice1.n == dice2.w and dice1.bottom == dice2.bottom): 
    print("Yes")
    exit()
  elif(dice1.top == dice2.top and dice1.s == dice2.n and dice1.e == dice2.w and dice1.w == dice2.e and dice1.n == dice2.s and dice1.bottom == dice2.bottom): 
    print("Yes")
    exit()
  elif(dice1.top == dice2.top and dice1.s == dice2.w and dice1.e == dice2.s and dice1.w == dice2.n and dice1.n == dice2.e and dice1.bottom == dice2.bottom): 
    print("Yes")
    exit()
##ans3 
top_1,s_1,e_1,w_1,n_1,bottom_1 = list(map(int,input().split()))
top_2,s_2,e_2,w_2,n_2,bottom_2 = list(map(int,input().split()))

##dice make
dice1 = dice(top_1,s_1,e_1,w_1,n_1,bottom_1)
dice2 = dice(top_2,s_2,e_2,w_2,n_2,bottom_2)
ans_3(dice1,dice2)

for i in range(4):
  dice2.roll("S")
  ans_3(dice1,dice2)

dice2.roll("E")
ans_3(dice1,dice2)
dice2.roll("E")
dice2.roll("E")
ans_3(dice1,dice2)
print("No")
