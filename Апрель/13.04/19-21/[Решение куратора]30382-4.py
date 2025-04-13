from functools import lru_cache


@lru_cache(None)
def game(a, b):
    if a + b <= 12:
        return 0
    moves = []
    if a > 0:
        moves.append(game(a - 1, b))
        moves.append(game(a // 2, b))
    if b > 0:
        moves.append(game(a, b - 1))
        moves.append(game(a, b // 2))
    win = [i for i in moves if i <= 0]
    if win:
        return -max(win) + 1
    else:
        return -max(moves)


func = lambda x: [s for s in range(4, 50) if game(9, s) == x]
print(min(func(-1)))  # 19
print(max(func(2)))  # 20
print(max(func(-2)))  # 21
