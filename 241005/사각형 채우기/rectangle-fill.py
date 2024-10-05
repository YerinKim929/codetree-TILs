n = int(input())
MOD = 10007


dp = [0]*(n+1)

for i in range(1, n+1):
    if i < 4:
        dp[i] = i
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[n])