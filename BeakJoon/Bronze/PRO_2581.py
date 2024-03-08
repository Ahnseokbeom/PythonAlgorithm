def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(m, n):
    prime_list = []
    for i in range(m, n + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

m = int(input())
n = int(input())

primes = find_primes(m, n)
if not primes:
    print(-1)
else:
    print("{0}\n{1}".format(sum(primes),min(primes)))
