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
    

top,s,e,w,n,bottom = list(map(int,input().split()))
direction = input()

dice1 = dice(top,s,e,w,n,bottom)
#dice1.test_dice()
for i in range(len(direction)):
  dice1.roll(direction[i])
#  dice1.test_dice()
dice1.ans_1()
