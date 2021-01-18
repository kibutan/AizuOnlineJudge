n = int(input())
cards = [list(map(str,input().split())) for _ in  range(n)]
#cards_taro =[]
#cards_hanako = []
point_taro = 0
point_hanako = 0 
for i in range(len(cards)):
#  cards_taro.append(cards[i][0])
#  cards_hanako.append(cards[i][1])
  if(cards[i][0] > cards[i][1]):point_taro += 3
  elif(cards[i][0] < cards[i][1]):point_hanako += 3
  else:
    point_taro += 1
    point_hanako += 1
#print(cards_taro)
#print(cards_hanako)
print(point_taro,end = " ")
print(point_hanako)
