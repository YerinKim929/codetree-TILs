n = int(input())
MOD = 10007

dp = [0] * (n+1)
dp[0] = 1

for i in range(2, n + 1):
    if i < 5:
        dp[i] = 1
        continue 
    dp[i] = (dp[i - 2] + dp[i - 3]) % MOD

print(dp[n])