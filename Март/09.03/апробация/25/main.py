def r(x):
    div = set()
    for j in range(2, x):
        if x % j == 0:
            div.add(j)
    return sum(div)


cnt = 0
for i in range(500_001, 1_000_000):
    if r(i) % 10 == 9:
        print(i, r(i))
        cnt += 1
    if cnt == 5:
        break
