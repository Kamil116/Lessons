f = open('26.txt')
m, n = map(int, f.readline().split())
queue = [list(map(int, request.split())) for request in f.readlines()]
queue.sort(key=lambda x: (x[0], -x[1]))
printers = [-1 for _ in range(m)]

with_delay = 0
last = 0
while queue:
    start, dur = queue.pop(0)
    min_free_time = min(printers)
    if start >= min_free_time:
        printers[printers.index(min_free_time)] = start + dur + 3
        last = start + dur
    else:
        end = min_free_time + dur + 3
        if min_free_time + dur <= 480:
            with_delay += 1
            printers[printers.index(min_free_time)] = end
print(with_delay, last)
# 791 75
