import sys
m = sys.stdin.readline().split()
tipud = int(m[0])
teed = int(m[1])
graaf = [[] for a in range(tipud)]
for b in range(teed):
    tee = sys.stdin.readline().split()
    c = int(tee[0])-1
    d = int(tee[1])-1
    graaf[c].append(d)
    graaf[d].append(c)
kaidud = [True for e in range(tipud)]
varvid = [True for f in range(tipud)]


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
                varvid[naaber] = not (varvid[hetkel])
            else:
                if varvid[hetkel] == varvid[naaber]:
                    return -1


for g in range(tipud):
    if kaidud[g]:
        otsing = laiuti_otsing(g)
        if otsing == -1:
            print("IMPOSSIBLE")
            exit(0)
tulemus = []
for h in varvid:
    if h:
        tulemus.append(str(1))
    else:
        tulemus.append(str(2))
print(" ".join(tulemus))

