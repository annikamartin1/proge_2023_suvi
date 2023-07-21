import sys
n = int(sys.stdin.readline())
dp = [sys.maxsize] * (n + 1)
dp[0] = 0
for i in range(1, (n + 1)):
    parim = sys.maxsize
    arv = str(i)
    for j in arv:
        j = int(j)
        parim = min(dp[i - j] + 1, parim)
    dp[i] = parim
print(dp[n])
