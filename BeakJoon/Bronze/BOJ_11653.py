def prime_primes(n):
    primes = []
    while n % 2 == 0:
        primes.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            primes.append(i)
            n //= i
    if n > 2: primes.append(n)
    return primes

N = int(input())

if N > 1:
    for factor in prime_primes(N): print(factor)
