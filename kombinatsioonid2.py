import sys
n = int(sys.stdin.readline())
korrad = [1, 2, 4, 8, 16, 32]
arv = 0
eelmine = 63
for i in range(7, n+1):
    if i == 7:
        korrad.append(63)
        continue
    arv = (eelmine*2 - korrad[i-8]) % 1000000007
    korrad.append(arv)
    eelmine = arv
tul = int(korrad[n-1])
print(tul)
