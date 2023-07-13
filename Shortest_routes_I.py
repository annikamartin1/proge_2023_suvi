import sys
m = sys.stdin.readline().split()
tipud = int(m[0])
teed = int(m[1])
graaf = [[]for a in range(tipud)]
kaalud = {}
kaidud = [True for x in range(tipud)]
jarg = 0
for c in range(teed):
    tee = sys.stdin.readline().split()
    d = int(tee[0]) - 1
    e = int(tee[1]) - 1
    f = int(tee[2])
    if e not in graaf[d]:
        graaf[d].append(e)
    if (d, e) in kaalud and kaalud[d, e] < f:
        kaalud[d, e] = kaalud[d, e]
    else:
        kaalud[d, e] = f
kaugused = [sys.maxsize for g in range(tipud)]
kaugused[0] = 0


def dijkstra(algus):
    for naaber in graaf[algus]:
        if kaidud[naaber]:
            if (algus, naaber) in kaalud:
                kaugused[naaber] = min(kaugused[naaber], kaugused[algus] + kaalud[algus, naaber])
            else:
                kaugused[naaber] = min(kaugused[naaber], kaugused[algus] + kaalud[naaber, algus])
    kaidud[algus] = False


for j in range(tipud):
    if kaidud[j]:
        vahim = min(kaugused[j:len(kaugused)])
        indeks = kaugused.index(vahim)
        while kaidud[indeks] == False:
            arv = kaugused[indeks]
            kaugused[indeks] = sys.maxsize
            vahim = min(kaugused[j:len(kaugused)])
            kaugused[indeks] = arv
            indeks = kaugused.index(vahim)
        dijkstra(indeks)
for l in kaugused:
    print(l, end=" ")
