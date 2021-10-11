numbers = [i for i in range(2,1000)]
primes = []
while numbers != []:
    p = numbers[0]
    primes.append(p)
    f = 1
    while f*p <= 1000:
        if f*p in numbers:
            numbers.remove(f*p)
        f += 1

#print(primes)

def prime_factors(n):
    factors = []
    #d = 2
    i = 0
    d = primes[0]
    while n > 1:
        if n % d == 0:
            n = n // d
            factors.append(d)
        else:
            #d += 1
            i += 1
            d = primes[i]
    return factors

print(prime_factors(150))
