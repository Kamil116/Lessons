from functools import lru_cache


@lru_cache(None)
def game(a, b, c):
    if a + b + c >= 150:
        return 0
    moves = [game(a + 16, b, c), game(a + 32, b, c), game(a * 2, b, c),
             game(a, b + 16, c), game(a, b + 32, c), game(a, b * 2, c),
             game(a, b, c + 16), game(a, b, c + 32), game(a, b, c * 2)]
    # +1 - из этой позиции можно ГАРАНТИРОВАННО выиграть за 1 ход
    # -1 - из это позиции 100% будет проигрыш за 1 ход
    # +2 - выигрыш за 2 хода
    win = [pos for pos in moves if pos <= 0]
    if win:
        return -max(win) + 1  # +2 -> -1 -> +1 -> 0
    else:
        return -max(moves)


for s in range(1, 67):
    if game(6, 2 * s, 3 * s) == -2:
        print(s)
