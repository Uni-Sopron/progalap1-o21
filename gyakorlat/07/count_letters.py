def count_letters(where):
    counts = {}
    for letter in where:
        if letter.isalpha():
            letter = letter.upper()
            counts[letter] = counts.get(letter, 0) + 1
    return counts

print(__name__)
if __name__ == '__main__':
    print(count_letters('ez egy meggyfa'))
