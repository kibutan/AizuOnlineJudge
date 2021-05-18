n,W = list(map(int,input().split()))
vw = [list(map(int,input().split())) for i in range(n)]
dp = [[0 for i in range(10001)] for j in range(101)]
for w in range(W):
    dp[0][w] = 0
for i in range(n):
    for w in range(W+1):
        # print("W >= vw[i][1]",W >= vw[i][1])
        if (w >= vw[i][1]):
            dp[i+1][w] = max(dp[i][w],dp[i][w - vw[i][1]]+vw[i][0],dp[i+1][w - vw[i][1]]+vw[i][0])
 #           print("if:","dp[",i,"][",w,"] = ",dp[i+1][w])
        else: 
            dp[i+1][w] = dp[i][w]
 #           print("else: ","dp[",i,"][",w,"] = ",dp[i][w])
print(dp[n][W])
