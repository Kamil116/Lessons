f = open('26var01.txt')
n, m, k = map(int, f.readline().split())
vert_rows = [m + 1 for _ in range(k + 1)]
for line in f.readlines():
    hor_row, vert_row = map(int, line.split())
    vert_rows[vert_row] = min(vert_rows[vert_row], hor_row)

min_hor_row = -100
min_vert_row = None
for i in range(len(vert_rows) - 1):
    free_hor_row = min(vert_rows[i], vert_rows[i + 1]) - 1
    if free_hor_row > min_hor_row:
        min_hor_row = free_hor_row
        min_vert_row = i
print(min_hor_row, min_vert_row)
