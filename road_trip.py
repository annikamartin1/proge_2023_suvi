import sys
sys.setrecursionlimit(100000)
tul = []
m = sys.stdin.readline().split()
tipud = int(m[0])
teed = int(m[1])
graaf = [[] for a in range(tipud)]
for b in range(teed):
    tee = sys.stdin.readline().split()
    c = int(tee[0]) - 1
    d = int(tee[1]) - 1
    graaf[c].append(d)
    graaf[d].append(c)
kaidud = [True for e in range(tipud)]
varvid = [True for f in range(tipud)]


def sygavuti_otsing(hetkel, eelmine):
    kaidud[hetkel] = False
    for sober in graaf[hetkel]:
        if kaidud[sober]:
            kaidud[sober] = False
            varvid[sober] = not varvid[hetkel]
            sygavuti_otsing(sober, hetkel)
            if len(tul) > 0:
                return
        else:
            if varvid[hetkel] == varvid[sober]:
                tul.append(0)
                return


for g in range(tipud):
    if kaidud[g]:
        sygavuti_otsing(g, g)
        if len(tul) > 0:
            print("IMPOSSIBLE")
            exit(0)

tulemus = []
for h in varvid:
    if h:
        print(1, end=" ")
    else:
        print(2, end=" ")
