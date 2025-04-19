f = open("task26__5z1ta.txt")
n, m, k = list(map(int, f.readline().split()))
places = [[] for i in range(k + 1)]
for i in f:
    ryad, mesto = map(int, i.split())
    places[mesto].append(ryad)
# del places[0]
t_ryad = 99999999999
for i in range(len(places) - 1):
    if places[i] and places[i + 1]:
        ma_1 = max(places[i])
        ma_2 = max(places[i + 1])
        ma_ryad = max(ma_1, ma_2) + 1
        if ma_ryad < t_ryad:
            t_ryad = ma_ryad

        if ma_ryad == 627:
            print(i, places[i])
            print(i + 1, places[i + 1])
print(t_ryad)
