N = int(sys.stdin.readline())
arvud = sys.stdin.readline().split()
paevi = int(sys.stdin.readline())
arvud_dict = {}
summa = 0
inflatsioon = 0
for a in arvud:
    inta = int(a)
    if inta in arvud_dict:
        arvud_dict[inta] = arvud_dict[inta] + 1
    else:
        arvud_dict[inta] = 1
    summa += inta

for i in range(paevi):
    tegevus = sys.stdin.readline().split()
    if tegevus[0] == "INFLATION":
        inflatsioon += int(tegevus[1])
        summa = summa + N * int(tegevus[1])
        print(summa)
    else:
        x = int(tegevus[1])
        y = int(tegevus[2])
        vana_vaartus_mis_dictionaris = x - inflatsioon
        uus_vaartus_mis_dictionaris = y - inflatsioon
        # kas üldse on
        if vana_vaartus_mis_dictionaris in arvud_dict:
            mitu_oli = arvud_dict[vana_vaartus_mis_dictionaris]
            # vota vana ära
            del arvud_dict[vana_vaartus_mis_dictionaris]
            # arvutama peame uue väärtusega
            summa = summa - mitu_oli * x

            #pane juurde
            if uus_vaartus_mis_dictionaris in arvud_dict:
                arvud_dict[uus_vaartus_mis_dictionaris] += mitu_oli
            else:
                arvud_dict[uus_vaartus_mis_dictionaris] = mitu_oli
            summa = summa + mitu_oli * y
            print(summa)
        else:
            print(summa)