def r(x):
    # сумма делителей, кроме единицы и себя
    divisors = set()
    for divisor in range(2, int(x ** 0.5) + 1):
        if x % divisor == 0:
            divisors.add(divisor)
            divisors.add(x // divisor)
    return sum(list(divisors))


cnt = 0
for i in range(500_001, 1_000_000):
    if r(i) % 10 == 9:
        cnt += 1
        print(i, r(i))
    if cnt == 5:
        break
