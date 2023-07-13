import sys
m = sys.stdin.readline().split()
tippe = int(m[0])
teed = int(m[1])
graaf = [[] for a in range(tippe)]
for i in range(teed):
    tee = sys.stdin.readline().split()
    b = int(tee[0]) - 1
    c = int(tee[1]) - 1
    graaf[b].append(c)
    graaf[c].append(b)
kaidud = [True for d in range(tippe)]
vanemad = []
for h in range(tippe):
    vanemad.append(h)



def laiuti_otsing(algus, lopp):
    Q = []
    Q.append(algus)
    kaidud[algus] = False
    while len(Q) != 0:
        hetkel = Q.pop(0)
        for naaber in graaf[hetkel]:
            if kaidud[naaber]:
                Q.append(naaber)
                kaidud[naaber] = False
                vanemad[naaber] = hetkel
            if naaber == lopp:
                return


otsing = laiuti_otsing(0, tippe-1)

if vanemad[tippe-1] == tippe-1:
    print("IMPOSSIBLE")
    exit(0)
indeks = tippe-1
tulemus = [str(indeks+1)]
while indeks != 0:
    tulemus.append(str(vanemad[indeks]+1))
    indeks = vanemad[indeks]
print(len(tulemus))
tulemus.reverse()
print(" ".join(tulemus))




