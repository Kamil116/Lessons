results = set()


def func(cur, moves_cnt=0):
    if moves_cnt == 8:
        results.add(cur)
        return
    func(cur + 1, moves_cnt + 1)
    func(cur + 4, moves_cnt + 1)
    func(cur * 2, moves_cnt + 1)


func(2)
print(len(results))
