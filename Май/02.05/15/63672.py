def f(n, m, k):
    if n + m > k and n + k > m and m + k > n:
        return 1
    else:
        return 0


u = []
for a in range(1, 1000):
    r = 0
    for x in range(1, 1000):
        y = not ((f(x, 6, 10) == (not (max(x, 7) > 35))) and f(x, a, 5))
        if y == 0:
            r = 1
            break
    if r == 0:
        u.append(a)
print(max(u))
