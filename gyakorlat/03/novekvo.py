max = int(input('Kerek egy szamot: '))
akt = int(input('Kerek egy szamot: '))
while akt > max:
    max = akt
    akt = int(input('Kerek egy szamot: '))
print('A novekvo sorozat maximuma:', max)
