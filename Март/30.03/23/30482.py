def func(cur, moves_count):
    if moves_count == 8:
        results.add(cur)
        return
    func(cur + 1, moves_count + 1)
    func(cur * 2, moves_count + 1)
    func(cur + 4, moves_count + 1)


results = set()
func(2, 0)
print(len(results))
