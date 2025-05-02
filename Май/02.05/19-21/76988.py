def f(x):
    if x >= 65:
        return 0
    n = [f(x + 7), f(x + 5)]
    if x * 3 < 109:
        n.append(f(x * 3))
    t = [int(i) for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)


for s in range(1, 40):
    if f(s) == 1:
        print(s)
