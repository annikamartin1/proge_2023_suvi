import sys
n = int(sys.stdin.readline())
korrad = [1, 2, 4, 8, 16, 32]
arv = 0
eelmine = 63
for i in range(7, n+1):
    for j in range(6):
        arv += korrad[i-(j+2)]
    korrad.append(arv % 1000000007)
    arv = 0
tul = int(korrad[n-1])
print(tul)
