import sys
m = sys.stdin.readline().split()
n = int(m[0])
x = int(m[1])
y = sys.stdin.readline().split()
myndid = [int(a) for a in y]
myndid.sort()

dp = [0] * (x + 1)
dp[0] = 1
for i in myndid:
    for j in range(x + 1):
        if dp[j] != 0 and j+i <= x:
            dp[j + i] = (dp[j + i] + dp[j]) % 1000000007
        if j+i > x:
            break
print(dp[x])

