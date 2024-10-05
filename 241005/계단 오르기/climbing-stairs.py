n = int(input())
MOD = 10007

dp = [0] * (n+1)

for i in range(2, n + 1):
    if i == 2 or i == 3:
        dp[i] = 1
        continue 
    dp[i] = dp[i - 2] + dp[i - 3]%MOD

print(dp[n])