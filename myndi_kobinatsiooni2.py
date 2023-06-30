import sys
m = sys.stdin.readline().split()
n = int(m[0])
loppsumma = int(m[1])
y = sys.stdin.readline().split()
myndid = [int(a) for a in y]
myndid.sort()

kogud = [0] * (loppsumma+1)
kogud[0] = 1
for i in myndid:
    for j in range(loppsumma+1):
        if kogud[j] != 0 and j+i <= loppsumma:
            kogud[j+i] = (kogud[j+i] + kogud[j]) % 1000000007
        if j+i > loppsumma:
            break
arv = kogud[loppsumma]
print(arv)

