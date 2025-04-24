def game(x):
    if x >= 65:
        return 0
    moves = [game(x + 7), game(x * 3), game(x + 5)]
    win = [i for i in moves if i <= 0]
    if win:
        return -max(win) + 1
    else:
        return -max(moves)


# П1: 22+
# В1: 21

for s in range(1, 40):
    if game(s) == -2:
        print(s)
