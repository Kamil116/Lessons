def func(cur, moves_count, moves):
    if moves_count > 12:
        return
    if moves_count == 12 and '11' not in moves and '22' not in moves:
        results.add(cur)
        return
    func(cur + 1, moves_count + 1, moves + '1')
    func(cur + 3, moves_count + 1, moves + '1')
    func(cur * 2, moves_count + 1, moves + '2')
    func(cur * 3, moves_count + 1, moves + '2')


results = set()
func(6, 0, '')
print(len(results))
