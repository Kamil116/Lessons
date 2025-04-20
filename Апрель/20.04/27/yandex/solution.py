from math import *
from turtle import tracer, goto, done, pu, dot


def dbscan(r, cur_star, all_stars, cluster):
    neighbours = []
    for i in range(len(all_stars)):
        if all_stars[i] != '*' and dist(all_stars[i], cur_star) <= r:
            neighbours.append(all_stars[i])
            cluster.append(all_stars[i])
            all_stars[i] = "*"
    for neighbour in neighbours:
        dbscan(r, neighbour, all_stars, cluster)
    return cluster


f = open('27_B.txt')
stars = []
for line in f.readlines():
    phi, r = map(float, line.split())
    # x = r * cos(ϕ)
    # y = r * sin(ϕ)
    x = r * cos(radians(phi))
    y = r * sin(radians(phi))
    stars.append([x, y])

# tracer(0)
# pu()
# m = 2
# for star in stars:
#     goto(star[0] * m, star[1] * m)
#     dot(5)
# # done()

clusters = []
for star in stars:
    if star != '*':
        clusters.append(dbscan(10, star, stars, []))

colors = ['red', 'blue', 'green', 'orange', 'cyan', 'magenta', 'black']
tracer(0)
pu()
m = 1
for cluster in clusters:
    for star in cluster:
        goto(star[0] * m, star[1] * m)
        dot(2, colors[clusters.index(cluster)])
done()

sx = sy = 0
for cluster in clusters:
    min_dist = 10 ** 10
    centroid = None
    for star in cluster:
        sum_dist = 0
        for other_star in cluster:
            sum_dist += dist(star, other_star)
        if sum_dist < min_dist:
            min_dist = sum_dist
            centroid = star
    sx += centroid[0]
    sy += centroid[1]
print(int(sx / len(clusters) * 10_000), int(sy / len(clusters) * 10_000))
# 10106 528042
