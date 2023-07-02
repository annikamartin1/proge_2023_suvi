import sys
n = int(sys.stdin.readline())
dp = [[0 for a in range(n+1)] for b in range(n+1)]
dp[0][1] = 1
for e in range(1, n+1):
    jarg = 1
    for h in sys.stdin.readline().strip():
        if h != "*":
            dp[e][jarg] += (dp[e - 1][jarg] + dp[e][jarg - 1]) % 1000000007
        jarg += 1
print(dp[n][n])
