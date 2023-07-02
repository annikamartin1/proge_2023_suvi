import sys
n = int(sys.stdin.readline())
korrad = [0] * (n+1)
korrad[0] = 1
arv = 0
eelmine = 63
for i in range(1, n+1):
    for j in range(6):
        if i-(j+1) < 0:
            continue
        else:
            arv += korrad[i-(j+1)]
    korrad[i] = (arv % 1000000007)
    arv = 0
tul = int(korrad[n])
print(tul)
