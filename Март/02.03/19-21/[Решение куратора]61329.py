def game(a, b):
    if 58 >= a + b >= 40:
        return 0
    if a + b > 58:
        return 1
    moves = [game(a + 2, b), game(a, b + 2), game(a * 2, b), game(a, b * 2)]
    wins = [i for i in moves if i <= 0]
    if wins:
        return -max(wins) + 1
    else:
        return -max(moves)


for s in range(1, 32):
    # 19
    # if game(8 + 1, s) == 1 or game(8, s + 1) == 1 or game(8 * 2, s) == 1 or game(8, s * 2) == 1:
    #     print(s)

    # 20
    if game(8, s) == -1:
        print(s)

    # 21
    # if game(8, s) == -2:
    #     print(s)
