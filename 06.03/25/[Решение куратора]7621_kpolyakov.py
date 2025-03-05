def m(x):
    divs = set()
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            divs.add(j)
            divs.add(x // j)
    if len(divs) == 0:
        return 0
    else:
        return max(divs) + min(divs)


cnt = 0
for i in range(800_001, 1_000_000):
    if m(i) % 10 == 4:
        print(i, m(i))
        cnt += 1
    if cnt == 5:
        break
