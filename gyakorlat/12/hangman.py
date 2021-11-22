from typing import Set

from hangman_backend import *

def show_correct(solution: str, guessed: Set[str]):
    dotted = ''
    #for i in range(len(solution)):
    #    dotted += '.'
    #dotted = '.' * len(solution)
    #for letter in guessed:
    #    for i in range(len(solution)):
    #        if letter == solution[i]:
    #            dotted = dotted[:i] + letter + dotted[i+1:]
    for i in range(len(solution)):
        if solution[i] in guessed:
            dotted += solution[i]
        else:
            dotted += '.'
    print(dotted)

def read_guess(guessed: Set[str]) -> str:
    while True:
        guess = input('guess a letter: ').upper()
        if len(guess) != 1 or not guess.isalpha():
            print('Error: guess must be a single letter')
            continue
        if guess in guessed:
            print('Error: this letter had been guessed already')
            continue
        break
    return guess

def main() -> None:
    # olvasd be a fajlbol a szavakat
    wordlist = read_words('words.txt')
    # valassz ki egy random szot
    solution = choose_word(wordlist)
    
    lives = 10
    guessed = set()
    while lives > 0 and not is_solved(solution, guessed):
        print('word:', end=' ')
        show_correct(solution, guessed)
        print('guessed letters:', lives)
        print('guessed letters:', ', '.join(guessed))
        guess = read_guess(guessed)
        guessed.add(guess)
        if not eval_guess(guess, solution):
            lives -= 1
    show_correct(solution, guessed)
    if lives == 0:
        print('you lost, the solution was', solution)
    else:
        print('you won!')

if __name__ == '__main__':
    main()