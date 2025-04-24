from functools import lru_cache


@lru_cache(None)
def game(a, b):
    if a >= 65 or b >= 65:
        return 0
    if a > b:
        moves = [game(a + 1, b), game(a + 2, b), game(a + 3, b), game(a, b * 2)]
    elif a < b:
        moves = [game(a, b + 1), game(a, b + 2), game(a, b + 3), game(a * 2, b)]
    else:
        moves = [game(a, b + 1), game(a, b + 2), game(a, b + 3)]

    wins = [i for i in moves if i <= 0]
    if wins:
        return -max(wins) + 1
    else:
        return -max(moves)


# 19
minim = 1000
for s in range(1, 100):
    for w in range(1, 100):
        if game(s, w) == 1:
            minim = min(minim, s + w)
print('19:', minim)

# 20
maxim = -100
minim = 100
for s in range(1, 65):
    if game(18, s) == 2:
        maxim = max(s, maxim)
        minim = min(minim, s)
print('20:', minim, maxim)

for s in range(1, 65):
    if game(26, s) == -2:
        print('21:', s)
