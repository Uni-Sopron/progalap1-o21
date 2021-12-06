# https://www.codingame.com/ide/puzzle/7-segment-scanner
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

line_1 = input()
line_2 = input()
line_3 = input()

digits = [' _ | ||_|', '     |  |', ' _  _||_ ', ' _  _| _|', '   |_|  |',
          ' _ |_  _|', ' _ |_ |_|', ' _   |  |', ' _ |_||_|', ' _ |_| _|']
number = ''
for i in range(len(line_1) // 3):
    digit = line_1[3*i:3*(i+1)] + line_2[3*i:3*(i+1)] + line_3[3*i:3*(i+1)]
    number += str(digits.index(digit))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(number)
