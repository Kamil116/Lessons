results = set()


def func(cur, moves_cnt=0, moves=''):
    if '22' in moves or '33' in moves:
        return
    if moves_cnt == 9:
        results.add(cur)
        return
    func(cur + 6, moves_cnt + 1, moves + '1')
    func(cur + 9, moves_cnt + 1, moves + '2')
    func(cur * 3, moves_cnt + 1, moves + '3')


func(3)
print(len(results))
