n,m = list(map(int,input().split()))
c = list(map(int,input().split()))

#求めるのが最小値なので初期化はでっかくする
dp=[[float("inf") for i in range(n+1)] for j in range(m)]

#0円を考えるときは0にする(0枚を考えるのはDIV0なので考えたくない)
#必ず1円もあるので1円を考えるときは1にする。
for i in range(m):
    dp[i][0] = 0
    dp[i][1] = 1

for i in range(m):
    for v in range(2,n+1):
        if(v >= c[i]):
            dp[i][v] = min(dp[i-1][v], dp[i][v-c[i]]+1)
        else:
            dp[i][v] = dp[i-1][v]


print(dp[i][v])

        
