from math import dist
from turtle import *


def dbscan(cur_star, r, all_stars, cluster):
    neighbours = []
    for i in range(len(all_stars)):
        if all_stars[i] != '*' and dist(all_stars[i], cur_star) < r:
            neighbours.append(all_stars[i])
            cluster.append(all_stars[i])
            all_stars[i] = '*'
    for neighbour in neighbours:
        dbscan(neighbour, r, all_stars, cluster)
    return cluster


# f = open('27-p00a.txt')
# clusters = []
# stars = [list(map(float, line.replace(',', '.').split())) for line in f.readlines()]
# for star in stars:
#     if star != '*':
#         clusters.append(dbscan(star, 1, stars, []))
#
# tracer(0)
# penup()
# cnt = 0
# colors = ['red', 'blue', 'purple']
# for cluster in clusters:
#     for star in cluster:
#         goto(star[0] * 50, star[1] * 30)
#         dot(3, colors[cnt])
#     cnt += 1
# update()
# mainloop()
#
# sx = sy = 0
# for i in range(len(clusters)):
#     centroid = None
#     minim = 10 ** 10
#     for star in clusters[i]:
#         sum_dist = 0
#         for star2 in clusters[i]:
#             sum_dist += ((star[0] - star2[0]) ** 2 + (star[1] - star2[1]) ** 2) ** 0.5
#         if sum_dist < minim:
#             minim = sum_dist
#             centroid = star
#     sx += centroid[0]
#     sy += centroid[1]
# print(int(sx / 2 * 10_000), int(sy / 2 * 10_000))

# Решение для файла Б
f = open('27-p00b.txt')
clusters = []
stars = [list(map(float, line.replace(',', '.').split())) for line in f.readlines()]
for star in stars:
    if star != '*':
        clusters.append(dbscan(star, 1, stars, []))

tracer(0)
penup()
cnt = 0
colors = ['red', 'blue', 'purple']
for cluster in clusters:
    for star in cluster:
        goto(star[0] * 50, star[1] * 30)
        dot(3, colors[cnt])
    cnt += 1
update()
mainloop()

sx = sy = 0
for i in range(len(clusters)):
    centroid = None
    minim = 10 ** 10
    for star in clusters[i]:
        sum_dist = 0
        for star2 in clusters[i]:
            sum_dist += ((star[0] - star2[0]) ** 2 + (star[1] - star2[1]) ** 2) ** 0.5
        if sum_dist < minim:
            minim = sum_dist
            centroid = star
    sx += centroid[0]
    sy += centroid[1]
print(int(sx / 3 * 10_000), int(sy / 3 * 10_000))
