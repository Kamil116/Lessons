from fnmatch import fnmatch


def is_prime(x):
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False
    return x > 1


primes = [x for x in range(2, 10 ** 5 + 1) if is_prime(x)]
super_primes = []
for i in range(len(primes)):
    if is_prime(i + 1):
        super_primes.append(primes[i])

for i in range(len(super_primes)):
    x = super_primes[i]
    if fnmatch(str(x), '1*7?7'):
        print(x, primes.index(x) + 1)
