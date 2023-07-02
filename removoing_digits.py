import sys
summa = int(sys.stdin.readline())
numbrid = set()
kogud = [sys.maxsize] * (summa+1)
kogud[0] = 0
for i in range(1, (summa+1)):
    parim = 999999999999
    hetk_parim = 0
    arv = str(i)
    for j in arv:
        j = int(j)
        hetk_parim = kogud[i-j]+1
        parim = min(hetk_parim, parim)
    kogud[i] = parim
print(kogud[summa])






