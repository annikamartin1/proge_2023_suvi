import sys
n = int(sys.stdin.readline())


def leia_kogus(n):
    if n == 0:
        return 1

    tul = 0
    for i in range(1, 7):
        if n - i >= 0:
            tul += leia_kogus(n-i)
    return tul


print(leia_kogus(n))
