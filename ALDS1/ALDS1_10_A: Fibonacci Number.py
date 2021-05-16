#Fibonacci Number
n = int(input())
dp = [0]*10000  #計算結果収納箱
inDp = [False]* 10000
dp[0] = 1
dp[1] = 1
inDp[0] = True
inDp[1] = True

def fibonacci(n):
  if(n == 0):return 1
  elif(n == 1):return 1
  else :return fibonacci(n-1) + fibonacci(n-2)  

def fibonacci_dp(n):
  for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n]

def fibonacci_memo(n):
  if not(inDp[n]):
    dp[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    inDp[n] = True 
  return dp[n]

print(fibonacci_memo(n))

