# https://www.codingame.com/ide/puzzle/graffiti-on-the-fence
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
nem_festett = [ (0,l) ]
n = int(input())
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    ujnf = []
    for nf in nem_festett:
        if ed <= nf[0] or nf[1] <= st:
            ujnf.append(nf)
        elif st <= nf[0] and ed >= nf[0] and ed < nf[1]:
            ujnf.append((ed, nf[1]))
        elif ed >= nf[1] and st <= nf[1] and st > nf[0]:
            ujnf.append((nf[0], st))
        elif st < nf[1] and st > nf[0] and ed > nf[0] and ed < nf[1]:
            ujnf += [(nf[0], st), (ed, nf[1])]
        else:
            pass
    nem_festett = ujnf

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if nem_festett:
    for nf in nem_festett:
        print(nf[0], nf[1])
else:
    print('All painted')