# Решение для файла А
# from math import dist
#
# f = open('27-66a.txt')
# clusters = [[] for _ in range(2)]
# for star in f.readlines():
#     x, y = map(float, star.replace(',', '.').split())
#     if y > 4 * x and x > -2.5:
#         clusters[0].append([x, y])
#     elif y < 4 * x and y > 3 / 2 * x - 2:
#         clusters[1].append([x, y])
#
# sx = sy = 0
# for cluster in clusters:
#     min_dist = 10 ** 10
#     centroid = None
#     for maybe_centroid in cluster:
#         cur_dist = 0
#         for star in cluster:
#             cur_dist += dist(star, maybe_centroid)
#         if cur_dist < min_dist:
#             min_dist = cur_dist
#             centroid = maybe_centroid
#     sx += centroid[0]
#     sy += centroid[1]
# print(int(sx / 2 * 10_000), int(sy / 2 * 10_000))

# Решение для файла Б
from math import dist

f = open('27-66b.txt')
clusters = [[] for _ in range(3)]
for star in f.readlines():
    x, y = map(float, star.replace(',', '.').split())
    if 0 < x < 3 and 4 < y < 9:
        clusters[0].append([x, y])
    elif y < -x + 10 and x > 2:
        clusters[1].append([x, y])
    elif y > -x + 10 and y > 4 and x > 4.5 and y < 7:
        clusters[2].append([x, y])

sx = sy = 0
for cluster in clusters:
    min_dist = 10 ** 10
    centroid = None
    for maybe_centroid in cluster:
        cur_dist = 0
        for star in cluster:
            cur_dist += dist(star, maybe_centroid)
        if cur_dist < min_dist:
            min_dist = cur_dist
            centroid = maybe_centroid
    sx += centroid[0]
    sy += centroid[1]
print(int(sx / 3 * 10_000), int(sy / 3 * 10_000))
