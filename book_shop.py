import sys
m = sys.stdin.readline().split()
n = int(m[0])
x = int(m[1])
h = sys.stdin.readline().split()
hinnad = [int(a) for a in h]
s = sys.stdin.readline().split()
lehed = [int(b) for b in s]
dp = [[0 for e in range(x + 1)] for c in range(n+1)]
jarg = 0
for i in hinnad:
    for j in range(x + 1):
        if j - i >= 0:
            dp[jarg+1][j] = max(dp[jarg][j], lehed[jarg] + dp[jarg][j-i])
        else:
            dp[jarg + 1][j] = dp[jarg][j]
    jarg += 1
print(dp[n][x])


