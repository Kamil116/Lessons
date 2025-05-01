f = open('26_17537.txt')
n, m, k = map(int, f.readline().split())
places = [[m + 1] for _ in range(k + 1)]
for i in range(n):
    row, place = map(int, f.readline().split())
    places[place].append(row)

max_row = 0
max_place = None
for i in range(1, k):
    if min(min(places[i]), min(places[i + 1])) - 1 >= max_row:
        max_row = min(min(places[i]), min(places[i + 1])) - 1
        max_place = i + 1

print(max_row, max_place)
