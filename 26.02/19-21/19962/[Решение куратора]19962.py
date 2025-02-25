from functools import lru_cache


@lru_cache()
def game(x, y):
    if x + y > 70:
        return 1
    if x + y >= 50:
        return 0
    moves = [game(x + 1, y), game(x * 2, y), game(x, y + 1), game(x, y * 2)]
    wins = [i for i in moves if i <= 0]
    if wins:
        return -max(wins) + 1
    else:
        return -max(moves)


for s in range(1, 30):
    if game(20, s) == -2:
        print(s)
