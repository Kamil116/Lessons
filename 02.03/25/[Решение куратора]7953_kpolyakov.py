from fnmatch import fnmatch


def a(n):
    str_n = str(n)
    if len(str_n) % 2 != 0:
        return 0

    first_half = str_n[:len(str_n) // 2]
    second_half = str_n[len(str_n) // 2:]
    summ = int(first_half) + int(second_half)
    return summ ** 2


for x in range(1, 35 * 10 ** 6):
    if a(x) == x and x % 25 == 0 and fnmatch(str(x), '*2*0*2*5*'):
        print(x, x // 25)
