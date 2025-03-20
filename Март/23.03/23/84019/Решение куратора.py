def func(a, b, flag, prev):
    if a > b or a == 18:
        return 0
    if a == b and flag:
        return 1
    if a == 6:
        flag = True
    if prev == 1:
        return func(a + 4, b, flag, 1) + func(a * 2, b, flag, 2)
    if prev == 2:
        return func(a * 2, b, flag, 2) + func(a * 3, b, flag, 3)
    return func(a + 4, b, flag, 1) + func(a * 2, b, flag, 2) + func(a * 3, b, flag, 3)


print(func(2, 296, False, 0))
