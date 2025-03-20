def is_prost(x):
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return False
    return True and x != 1


# x = p**6
primes = [prime for prime in range(3, int(123456789 ** (1 / 6) + 1)) if is_prost(prime)]
cnt = 0
for prime in primes:
    for k in range(0, 31):
        x = prime ** 6 * 2 ** k
        if 1000 <= x <= 123456789:
            cnt += 1
print(cnt)
