f = open('task26__5z1ta.txt')
n, m, k = map(int, f.readline().split())
places = [-1 for _ in range(k + 1)]
# храним для каждого места максимальный номер ряда,
# в котором это место занято

for i in range(n):
    row, place = map(int, f.readline().split())
    places[place] = max(places[place], row)

min_row = 10 ** 10
min_place = -1
for i in range(len(places) - 1):
    if max(places[i], places[i + 1]) + 1 < min_row:
        min_row = max(places[i], places[i + 1]) + 1
        min_place = i
print(min_row, min_place)
