from typing import List
from typing import Set

import random

def read_words(filename: str) -> List[str]:
    with open(filename) as f:
        words = [word.strip() for word in f]
    return words

def choose_word(wordlist: List[str]) -> str:
    #n = len(wordlist)
    #index = random.randrange(n)
    #return wordlist[index]
    return random.choice(wordlist).upper()

def eval_guess(guess: str, solution: str) -> bool:
    pass

def is_solved(solution: str, guessed: Set[str]) -> bool:
    pass