# olvassunk be egy szamot es mondjuk meg, hogy paros szam-e
szam = int(input('szam = '))
if szam % 2 == 1:
	print('paratlan')
else:
	print('paros')
# mondjuk meg, hogy primszam-e
oszto = 2
while oszto ** 2 < szam and szam % oszto != 0:
	oszto = oszto + 1
if oszto >= szam ** 0.5:
	print('prim')
else:
	print('nem prim, osztoja:', oszto)

# h.f.:
# meddig kell novelni az osztot?
# primtenyezos felbontas
# lnko
