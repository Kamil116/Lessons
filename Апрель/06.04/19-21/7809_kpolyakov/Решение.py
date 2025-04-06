# Классика
from functools import lru_cache


@lru_cache(None)
def game(x, y):
    if x + y >= 174:
        return 0
    moves = [game(x + 1, y), game(x, y + 1), game(x + 3, y), game(x, y + 3), game(x * 2, y), game(x, y * 2)]
    win = [i for i in moves if i <= 0]
    if win:
        return -max(win) + 1
    else:
        return -max(moves)


print(min([i for i in range(1, 155) if
           game(19 + 1, i) == 1 or game(19, i + 1) == 1 or
           game(19 + 3, i) == 1 or game(19, i + 3) == 1 or
           game(19 * 2, i) == 1 or game(19, i * 2) == 1]))  # 19
print(*[i for i in range(1, 155) if game(19, i) == 2])  # 20
print(*[i for i in range(1, 155) if game(19, i) == -2])  # 21

# # Решение Кати
# def f(s1, s2, m):
#     if (s1 + s2) >= 174: return m % 2 == 0
#     if m == 0: return 0
#     h = [f(s1 + 1, s2, m - 1), f(s1 * 2, s2, m - 1), f(s1, s2 + 1, m - 1), f(s1, s2 * 2, m - 1), f(s1, s2 + 3, m - 1),
#          f(s1 + 3, s2, m - 1)]
#     return any(h) if (m - 1) % 2 == 0 else all(h)
#
#
# print([s for s in range(1, 155) if f(s, 19, 2)])  # Примечание куратора: нужно ещё в функции заменить all на any
# print([s for s in range(1, 155) if f(s, 19, 3) and (not f(s, 19, 1))])
# print([s for s in range(1, 155) if f(s, 19, 4) and (not f(s, 19, 2))])
