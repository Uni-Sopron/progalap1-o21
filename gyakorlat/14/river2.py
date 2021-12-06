# https://www.codingame.com/ide/puzzle/the-river-ii-
import sys
import math

from river1 import digitsum

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


if __name__ == "__main__":
    r_1 = int(input())
    digitcount = len(str(r_1))
    for i in range(1, 9 * digitcount + 1):
        if digitsum(r_1-i) == i:
            print("YES")
            exit()

    # Write an answer using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    print("NO")
