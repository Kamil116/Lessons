def game(x, y):
    if (x ** 2 + y ** 2) ** 0.5 > 14:
        return 0
    moves = [game(2 * x, y), game(x, y + 3), game(x, y + 4)]
    win = [i for i in moves if i <= 0]
    if win:
        return -max(win) + 1
    else:
        return -max(moves)


for s in range(1, 14):
    if game(3, s) == -2:
        print(s)
