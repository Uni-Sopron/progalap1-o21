# https://www.codingame.com/ide/puzzle/the-river-i-
import sys
import math

def digitsum(n: int) -> int:
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

if __name__ == "__main__":
    r_1 = int(input())
    r_2 = int(input())

    while r_1 != r_2:
        if r_1 < r_2:
            r_1 += digitsum(r_1)
        else:
            r_2 += digitsum(r_2)

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print(r_1)
