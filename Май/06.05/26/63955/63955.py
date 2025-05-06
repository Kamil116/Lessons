f = open('Задание_27__1vtrl.txt')
m, n = map(int, f.readline().split())
categories = list(map(int, f.readline().split()))
places = []
for i in range(m):
    places.append([[] for _ in range(categories[i])])

clients = [list(map(int, i.split())) for i in f]
clients.sort()
for client in clients:
    start, duration, num_category = client
    found_place = False
    for i in range(num_category, m):
        for j in range(len(places[i])):
            if not places[i][j] or max(places[i][j]) <= start:
                places[i][j].append(start + duration)
                found_place = True
                break
        if found_place:
            break

max_total_places = 0
max_places_ind = 0
for i in range(m):
    total_places = 0
    for j in range(len(places[i])):
        total_places += len(places[i][j])
    if total_places > max_total_places:
        max_total_places = total_places
        max_places_ind = i

latest_time = 0
for i in range(len(places[max_places_ind])):
    latest_time = max(latest_time, places[max_places_ind][i][-1])
print(latest_time, max_total_places)
