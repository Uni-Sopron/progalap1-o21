n = int(input())
bin = ''
while n > 0:
    #print(n % 2, end='')
    #bin = str(n % 2) + bin
    bin += str(n % 2)
    n //= 2
#print(bin)
print(bin[::-1])
