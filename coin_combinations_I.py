import sys
m = sys.stdin.readline().split()
n = int(m[0])
x = int(m[1])
coins = sys.stdin.readline().split()
myndid = [int(a) for a in coins]

dp = [0] * (x + 1)
dp[0] = 1
for i in range(x + 1):
    if dp[i] != 0:
        for j in myndid:
            if i+j <= x:
                dp[i + j] = (dp[i] + dp[i + j]) % 1000000007
print(dp[x])
