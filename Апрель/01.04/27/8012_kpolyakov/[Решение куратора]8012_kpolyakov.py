# для файла А
from math import dist

f = open('27-79a.txt')
clusters = [[] for _ in range(4)]
for line in f.readlines():
    star = list(map(float, line.replace(',', '.').split()))
    x, y = star
    if x < 0 and y > 0:
        clusters[0].append(star)
    elif y < 0 and -2 < x < 2:
        clusters[1].append(star)
    elif x > 3 and y < 2:
        clusters[2].append(star)
    else:
        clusters[3].append(star)

diameters = []
for cluster in clusters:
    mn = -10 ** 10
    for first_star in cluster:
        for second_star in cluster:
            mn = max(mn, dist(first_star, second_star))
    diameters.append(mn)
print(int(min(diameters) * 100_000), int(sum(diameters) / len(diameters) * 100_000))
print(17 ** 6)
