import sys
n = int(sys.stdin.readline())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    arv = 0
    for j in range(1, 7):
        if i - j >= 0:
            arv += dp[i - j]
            dp[i] = (arv % 1000000007)
print(dp[n])
