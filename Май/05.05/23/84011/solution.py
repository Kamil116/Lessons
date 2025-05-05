def f(a, b, moves=''):
    if a > b or '11' in moves or '22' in moves or '33' in moves:
        return 0
    if a == b:
        return 1
    return f(a + 8, b, moves + '1') + f(a * 3, b, moves + '2') + f(a + a % 10, b, moves + '3')


print(f(4, 174))
