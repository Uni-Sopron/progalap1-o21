sorarak = {}
with open('arak.txt', encoding='utf-8') as f:
    for line in f:
        words = line.strip().split()
        price = int(words[-1])
        name = words[0]
        for w in words[1:-1]:
            name += ' ' + w
        name = ' '.join(words[:-1])
        sorarak[name.lower()] = price

total_price = 0
while True:
    beer = input("Choose a beer: ").lower()
    if beer == 'exit':
        break
    if beer in sorarak:
        total_price += sorarak[beer]
    else:
        print('Beer not found.')
    print("Total price:", total_price)
