def f(n, m, k):
    t = sorted([n, m, k])
    n = t[0]
    m = t[1]
    k = t[2]
    return 1 if n + m > k else 0


u = []
for a in range(1, 1000):
    r = 0
    for x in range(1, 1000):
        y = not ((f(x, 6, 10) == (not (max(x, 7) > 35))) and f(x, a, 5))
        if y == 0:
            r = 1
    if r == 0:
        u.append(a)
print(max(u))
