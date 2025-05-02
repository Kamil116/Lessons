f = open('26_3__6gp6u.txt')
n, m, k = map(int, f.readline().split())
places = [[m + 1] for _ in range(k + 1)]
for i in range(n):
    row, place = map(int, f.readline().split())
    places[place].append(row)

max_row = 0
min_place = None
for i in range(1, len(places) - 1):
    if min(min(places[i]), min(places[i + 1])) - 1 > max_row:
        max_row = min(min(places[i]), min(places[i + 1])) - 1
        min_place = i
print(max_row, min_place)
