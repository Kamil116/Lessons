from copy import deepcopy

f = open('task26__5z1t6.txt')
n, m, k = map(int, f.readline().split())
places = [[m + 1] for _ in range(k + 1)]
for i in range(n):
    row, place = map(int, f.readline().split())
    places[place].append(row)
occupied = deepcopy(places)
free_places = []
for i in range(len(places)):
    places[i].sort()
    if len(places[i]) >= 3:
        places[i].pop(0)
        places[i].pop(0)

        cur = places[i][0] - 1
        while cur in occupied[i]:
            cur -= 1
        free_places.append(cur)
    elif len(places[i]) == 2:
        places[i].pop(0)

        cur = places[i][0] - 1
        while cur in occupied[i]:
            cur -= 1
        free_places.append(cur)
    else:
        free_places.append(m)

maxim = 0
max_place = None
for i in range(1, k):
    max_row = min(free_places[i], free_places[i + 1])
    while max_row in occupied[i] or max_row in occupied[i + 1]:
        max_row -= 1
    if max_row >= maxim:
        maxim = max_row
        max_place = i + 1
print(maxim, max_place)
