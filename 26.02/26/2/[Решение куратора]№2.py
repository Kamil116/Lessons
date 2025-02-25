f = open('26-60.txt')
k, n = map(int, f.readline().split())

available_places = []
for i in range(k):
    available_places.append(int(f.readline()))

specialities = dict()
for i in range(k):
    specialities[i] = []

for i in range(n):
    points, spec = map(int, f.readline().split())
    specialities[spec].append(points)

passed = 0
for spec in specialities:
    points_list = specialities[spec]
    points_list.sort(reverse=True)
    rem = available_places[spec]
    for i in range(len(points_list)):
        if rem > 0:
            passed += 1
            rem -= 1

print(passed, end=' ')

max_students = 0
min_point = 0
for spec in specialities:
    points_list = specialities[spec]
    points_list.sort(reverse=True)
    rem = available_places[spec]
    min_cur = 0
    for i in range(len(points_list)):
        if rem > 0:
            rem -= 1
            min_cur = points_list[i]

    if len(points_list) / available_places[spec] > max_students:
        max_students = len(points_list) / available_places[spec]
        min_point = min_cur

print(min_point)
