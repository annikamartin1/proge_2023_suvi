import sys
k = int(sys.stdin.readline())
n = int(sys.stdin.readline())
v = sys.stdin.readline().split()
sambad = [int(a) for a in v]
summa = k+2300
dp = [[[0, 101] for b in range(summa)] for c in range(n+1)]
jarg = 0
for i in sambad:
    dp[jarg][0] = [1, 0]
    for j in range(summa):
        if i+j >= summa:
            break
        if dp[jarg][j][0] != 0:
            dp[jarg+1][j][0] = dp[jarg][j][0]
            dp[jarg + 1][j][1] = min(dp[jarg + 1][j][1], dp[jarg][j][1])
            if dp[jarg+1][i+j][0] != 0:
                dp[jarg+1][i+j][1] = min((dp[jarg][j][1] + 1), (dp[jarg+1][i+j][1]))
            else:
                dp[jarg+1][i+j][0] = dp[jarg+1][j][0] + j
                dp[jarg+1][i+j][1] = dp[jarg][j][1] + 1
    jarg += 1
tul = 0
mitu = 0
mitmes = 0
for e in dp[n]:
    if mitmes == 0 or mitmes < k:
        mitmes += 1
        continue
    if e[0] != 0 and abs(k-tul) > abs(k-mitmes):
        mitu = e[1]
        tul = mitmes
    mitmes += 1
print(mitu, tul)
