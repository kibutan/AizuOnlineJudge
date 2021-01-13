n = int(input())
mark_list = ["S","H","C","D"]
card_list = []
for i in mark_list:
  for j in range(13):
    card_list.append([i,str(j+1)])
print(card_list)

list = []
for _ in range(n):
  a,b = map(str, input().split())
  print([a,b])
  set(card_list)^set([a,b])
print("ans",card_list)
