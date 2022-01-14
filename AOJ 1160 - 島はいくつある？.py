import sys
sys.setrecursionlimit(10**7)
w = -1
h = -1

def dfs(y,x):
    if((y,x) not in arrived):
        arrived.append((y,x))
        for i in range(-1,2):
            for j in range(-1, 2):
                if(c[y+i][x+j] == 1):dfs(y+i,x+j)

    #再帰
    # if 8方でまだ見てないところに1がある
    # dfs(n)
    # else
    # return しなくてもいいかも。
    # すべての1が[Arrived]になったとき、dfs(n) が再帰以外で呼ばれた回数が答え


    # return True
ans = []
while w != 0 and h != 0:
    w,h =  map(int,sys.stdin.readline().split())

    cnt = 0
    arrived = []
    # print(w)
    # exit()
    if w == 0 and h == 0:
        for i in ans:
            print(i)
        exit()
    else:
        # 上下左右に0を入れてみる
        c = [[0] + list(map(int,input().split())) +[0] if (i > 0 and i < h+1) else [0 for j in range(w+2)] for i in range(0,h+2)]
        for i in range(1,h+1):
            for j in range(1,w+1):
                if(c[i][j] == 1 and (i,j) not in arrived):
                    dfs(i,j)
                    cnt += 1
        # print("cnt",cnt)
        ans.append(cnt)
