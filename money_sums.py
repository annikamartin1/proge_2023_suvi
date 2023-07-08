import sys
n = int(sys.stdin.readline())
coins = sys.stdin.readline().split()
myndid = [int(a) for a in coins]
summa = sum(myndid)
dp = [[0 for e in range(summa+1)] for c in range(n+1)]
dp[0][0] = 1
jarg = -1
for i in myndid:
    jarg += 1
    dp[jarg][0] = 1
    for j in range(summa+1):
        if dp[jarg][j] != 0:
            dp[jarg+1][j] = 1
            dp[jarg+1][j+i] = 1
vastus = 0
arvud = []
jarg = 0
for tul in dp[n]:
    if jarg == 0:
        jarg += 1
        continue
    if tul == 1:
        vastus += 1
        arvud.append(str(jarg))
    jarg += 1
print(vastus)
print(" ".join(arvud))




