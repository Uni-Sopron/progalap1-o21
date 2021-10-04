# olvassunk be 5 egesz szamot, majd irjuk ki oket forditott sorrendben

lista = []
for i in range(5):
    szam = int(input('adjon meg egy szamot: '))
    lista.append(szam)
#lista.reverse()
print(list(reversed(lista)))

# olvassunk be 1 egesz szamot, es toroljuk ki minden elofordulasat a listabol, majd irjuk ki az igy kapott listat

szam = int(input('adja meg a torlendo szamot: '))

#while szam in lista:
#    lista.remove(szam)
#print(lista)

#for i in range(len(lista)):
i = 0
while i < len(lista):
    if lista[i] == szam:
        lista.pop(i)
    else:
        i += 1
print(lista)

# az egymast koveto egyforma ertekekbol csak 1 maradjon a listaban, a tobbit toroljuk

i = 1
while i < len(lista):
    if lista[i] == lista[i-1]:
        lista.pop(i)
    else:
        i += 1
print(lista)