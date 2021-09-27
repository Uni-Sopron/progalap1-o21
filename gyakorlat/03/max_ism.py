akt = int(input('szam: '))
ism_szam = 1
max = 1
ismetlodo = akt
while akt != 0:
    elozo = akt
    akt = int(input('szam: '))
    if akt != elozo:
        ism_szam = 1
    else:
        ism_szam = ism_szam + 1
        if ism_szam > max:
            max = ism_szam
            ismetlodo = akt
print(max, "db", ismetlodo)
