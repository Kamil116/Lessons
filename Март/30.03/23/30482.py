results = set()


def f(cur, moves_cnt):
    if moves_cnt == 8:
        results.add(cur)
        return
    f(cur + 1, moves_cnt + 1)
    f(cur * 2, moves_cnt + 1)
    f(cur + 4, moves_cnt + 1)


f(2, 0)
print(len(results))
