# olvassunk be egy mondatot
# irjuk ki, hogy az egyes betuk hanyszor szerepelnek a mondatban
#sentence = input()
sentence = 'ez egy meggyfa'

# szamoljuk meg az 1. betu elofordulasait
counter = 0
for letter in sentence:
    if letter == sentence[0]:
        counter += 1
print(f'elso betu: {sentence[0]}: {counter} db')
#counter = sentence.count(sentence[0])
#print(f'{sentence[0]}: {counter} db')

# listaval:
def count_letter(to_count, where):
    counter = 0
    for letter in where:
        if letter == to_count:
            counter += 1
    return counter

# halmazzal:
letters = set()
for letter in sentence:
    if letter != ' ' and letter not in letters:
        count = count_letter(letter, sentence)
        print(f'{letter}: {count} db')
        letters.add(letter)
print(letters)

# szotarral, fuggvenykent:
def count_letters(where):
    counts = {}
    for letter in where:
        if letter != ' ':
            #if letter not in counts:
            #    counts[letter] = 1
            #else:
            #    counts[letter] += 1
            counts[letter] = counts.get(letter, 0) + 1
    return counts

counts = count_letters(sentence)
for letter,count in counts.items():
    print(f'{letter}: {count} db')
