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

tulemused = []
laiuti_otsing(0)
for j in range(tipud):
    if kaidud[j]:
        otsing = laiuti_otsing(j)
        tulemused.append(j+1)

print(len(tulemused))
for f in tulemused:
    print(1, f)
