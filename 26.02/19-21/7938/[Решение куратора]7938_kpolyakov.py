from functools import lru_cache


@lru_cache()
def game(x):
    if x >= 132:
        return 0
    moves = [game(x + 3), game(x + 6), game(x * 3)]
    wins = [i for i in moves if i <= 0]
    if wins:
        return -max(wins) + 1
    else:
        return -max(moves)


for s in range(1, 132):
    if game(s) == -2:
        print(s)
