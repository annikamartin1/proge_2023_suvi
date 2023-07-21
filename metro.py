import sys
m = sys.stdin.readline().split()
tipud = int(m[0])
alice = int(m[1])
graaf = [[] for a in range(tipud*2)]
edasi = sys.stdin.readline().split()
kaidud = [True for x in range(tipud*2)]
if edasi[0] == "0":
    print("NO")
    exit(0)
tagasi = sys.stdin.readline().split()
if edasi[alice-1] == "0" and tagasi[alice-1] == "0":
    print("NO")
    exit(0)
ylemine = []
alumine = []
jarg = 0
for c in edasi:
    if int(c) == 1:
        ylemine.append(jarg)
    if int(tagasi[jarg]) == 1 and int(c) == 1:
        graaf[jarg].append(jarg+tipud)
        graaf[jarg+tipud].append(jarg)
    jarg += 1
jarg = 0
for d in tagasi:
    if int(d) == 1:
        alumine.append(jarg+tipud)
    jarg += 1

for i in range(tipud):
    for j in ylemine:
        if j > i:
            if edasi[i] != "0":
                graaf[i].append(j)
alumine.reverse()
for h in range(tipud):
    if tagasi[tipud-(h+1)] == "0":
        continue
    for g in alumine:
        if g < tipud*2-(h+1):
            graaf[tipud*2-(h+1)].append(g)


def laiuti_otsing(algus, lopp):
    Q = []
    Q.append(algus)
    kaidud[algus] = False
    while len(Q) != 0:
        hetkel = Q.pop(0)
        for naaber in graaf[hetkel]:
            if naaber == lopp or naaber == tipud+lopp:
                return 1
            if kaidud[naaber]:
                Q.append(naaber)
                kaidud[naaber] = False
    return -1

tul = laiuti_otsing(0,alice-1)
if tul == 1:
    print("YES")
else:
    print("NO")



