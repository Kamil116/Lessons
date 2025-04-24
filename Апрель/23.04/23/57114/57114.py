results = set()


def func(cur, moves_cnt, moves):
    if '11' in moves or '22' in moves or '33' in moves:
        return
    if moves_cnt == 13:
        results.add(cur)
        return
    func(cur + 2, moves_cnt + 1, moves + '1')
    func(cur + 5, moves_cnt + 1, moves + '2')
    func(cur * 2, moves_cnt + 1, moves + '3')


func(8, 0, '')
print(len(results))
