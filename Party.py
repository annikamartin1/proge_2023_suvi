import sys
tipud = int(sys.stdin.readline())
graaf = [[] for a in range(tipud)]
boss = []
for b in range(tipud):
    tootaja = int(sys.stdin.readline()) - 1
    if tootaja >= 0:
        graaf[tootaja].append(b)
    else:
        boss.append(b)
kaidud = [True for c in range(tipud)]
sygavus = [1 for d in range(tipud)]


def laiuti_otsing(algus):
    Q = []
    Q.append(algus)
    kaidud[algus] = False
    while len(Q) != 0:
        hetkel = Q.pop(0)
        for naaber in graaf[hetkel]:
            if kaidud[naaber]:
                kaidud[naaber] = False
                Q.append(naaber)
                sygavus[naaber] = sygavus[hetkel] + 1

for j in boss:
    laiuti_otsing(j)
print(max(sygavus))

