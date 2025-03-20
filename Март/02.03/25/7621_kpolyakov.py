# Решение Марселя
def dM(n):
    d = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
                break
    if len(d) > 0:
        return max(d) + min(d)
    else:
        return 0


k = 0
for n in range(800000, 10 ** 10):
    M = dM(n)
    if M % 10 == 4 and M != 0:
        k += 1
        print(n, M)
        if k == 5:
            break
