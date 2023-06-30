import sys
m = sys.stdin.readline().split()
rida = int(m[0])
veerg = int(m[1])
pold = [[[] for a in range(veerg)] for b in range(rida)]
for c in range(rida):
    jarg = 0
    for d in sys.stdin.readline().split():
        pold[c][jarg] = int(d)
        jarg += 1
parim_tul = 0
for i in range(rida):
    for j in range(veerg):
        abi_pold = [[0 for a in range(veerg)] for b in range(rida)]
        for k in range(i, rida):
            jooksev_rida = 0
            for l in range(j, veerg):
                jooksev_rida += pold[k][l]
                eelmine = 0
                if k != 0:
                    eelmine = abi_pold[k-1][l]
                abi_pold[k][l] = jooksev_rida + eelmine
                hetk_parim = jooksev_rida + eelmine
                parim_tul = max(parim_tul, hetk_parim)

print(parim_tul)
