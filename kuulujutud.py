import sys
sys.setrecursionlimit(100000)
m = sys.stdin.readline().split()
mitu = int(m[0])
gruppe = int(m[1])
jutud = int(m[2])
vanemad = []
suurused = []
for a in range(mitu):
    vanemad.append(a)
    suurused.append(1)


def leia_vanem(indeks):
    if vanemad[indeks] == indeks:
        return indeks
    else:
        vanem = leia_vanem(vanemad[indeks])
        vanemad[indeks] = vanem
        return vanem


def kokku_panemine(yks, kaks):
    yks_vanem = leia_vanem(yks)
    kaks_vanem = leia_vanem(kaks)
    if yks_vanem != kaks_vanem:
        if suurused[yks_vanem] > suurused[kaks_vanem]:
            vanemad[kaks_vanem] = yks_vanem
            suurused[yks_vanem] += suurused[kaks_vanem]
        else:
            vanemad[yks_vanem] = kaks_vanem
            suurused[kaks_vanem] += suurused[yks_vanem]


for b in range(gruppe):
    grupp = sys.stdin.readline().split()
    suurus = int(grupp[0])
    essa = int(grupp[1])-1
    for c in range(suurus-1):
        sober = int(grupp[c+2])-1
        kokku_panemine(essa, sober)

for d in range(jutud):
    teab = int(sys.stdin.readline().strip())-1
    print(suurused[leia_vanem(teab)])
