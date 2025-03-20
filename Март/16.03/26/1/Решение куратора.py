f = open('26.txt')
n = int(f.readline())
places = [[] for _ in range(10_001)]
for i in range(n):
    row, place = map(int, f.readline().split())
    places[row].append(place)

answers = []
for i in range(len(places)):
    places[i].sort()
    min_place = None
    for j in range(len(places[i]) - 1):
        if places[i][j + 1] - places[i][j] >= 5:
            min_place = places[i][j] + 3
            break
    if min_place:
        answers.append([i, min_place])
print(*answers[-1])
