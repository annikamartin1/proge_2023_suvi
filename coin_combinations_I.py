import sys
m = sys.stdin.readline().split()
n = int(m[0])
loppsumma = int(m[1])
y = sys.stdin.readline().split()
myndid = [int(a) for a in y]
kogud = [0] * (loppsumma+1)
kogud[0] = 1
for i in range(loppsumma+1):
    if kogud[i] == 0:
        continue
    for j in myndid:
        if i+j <= loppsumma:
            kogud[i+j] = (kogud[i] + kogud[i+j]) % 1000000007

print(kogud[loppsumma])


