import sys
m = sys.stdin.readline().split()
n = int(m[0])
loppsumma = int(m[1])
y = sys.stdin.readline().split()
myndid = [int(a) for a in y]
kogud = [sys.maxsize] * (loppsumma+1)
kogud[0] = 0
for i in range(loppsumma+1):
    if kogud[i] == sys.maxsize:
        continue
    for j in myndid:
        if i+j <= loppsumma:
            kogud[i+j] = min(kogud[i]+1, kogud[i+j])
if kogud[loppsumma] == sys.maxsize:
    print(-1)
else:
    print(kogud[loppsumma])

