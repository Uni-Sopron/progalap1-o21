# be: a,b (pozitiv egeszek)
# ki: lnko(a,b)

a, b = int(input()), int(input())

if b < a:
    # c = b
    # b = a
    # a = c
    a, b = b, a

while a > 0:
    c = b % a
    if c == 0:
        print('lnko =', a)
    b = a
    a = c
