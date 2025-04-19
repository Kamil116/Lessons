from functools import lru_cache


@lru_cache(None)
def game(x):
    if x <= 7:
        return 0
    moves = [game(x - 1), game(x - 3)]
    wins = [i for i in moves if i <= 0]
    if wins:
        return -max(wins) + 1
    else:
        return -max(moves)


for s in range(8, 100):
    if (game(s) == 1 or game(s) == 2
            and (game(s - 1) == 1 or (game(s - 3) == 1))):
        print(s)
