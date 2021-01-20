card_list = []
for i in ["S","H","C","D"]:
  for j in range(13):
    card_list.append([i,str(j+1)])
#print(card_list)
n = int(input())
cards = [list(map(str,input().split())) for _ in range(n)]
#print(cards)

for k in cards:
  card_list.remove(k)

for l in card_list:
  print(*l)
