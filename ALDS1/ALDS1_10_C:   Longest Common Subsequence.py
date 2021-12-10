n = int(input())
for query in range(n):
    x = input()
    y = input()
    len_x = len(x)
    len_y = len(y)
    # dp = [[0 for i in range(len_y+1)] for j in  range(len_x+1)]
    l=[]
    for yk in y:
        bgn_idx = 0
        for i,cur_idx in enumerate(l):
            char_idx = x.find(yk,bgn_idx) + 1
            if not char_idx:break
            l[i] = min(cur_idx,char_idx)
            bgn_idx = cur_idx
        else:
            char_idx = x.find(yk,bgn_idx) + 1
            if char_idx:l.append(char_idx)
    print(len(l))
