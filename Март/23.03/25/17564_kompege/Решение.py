def m(x):
    divs = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.add(i)
            divs.add(x // i)
    if len(divs) == 0:
        return 0
    else:
        return max(divs) + min(divs)


cnt = 0
for i in range(700_001, 1_000_000):
    if m(i) % 10 == 4:
        print(i, m(i))
        cnt += 1
        if cnt == 5:
            break
