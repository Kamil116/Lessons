from functools import lru_cache


@lru_cache(None)
def game(x):
    if x >= 68:
        return 0
    moves = [game(x + 2), game(x + 4), game(x * 3)]
    wins = [pos for pos in moves if pos <= 0]
    if wins:
        return -max(wins) + 1
    else:
        return -max(moves)


for s in range(1, 68):
    if game(s + 2) == 1 or game(s + 4) == 1 or game(s * 3) == 1:
        print(s)
        break
