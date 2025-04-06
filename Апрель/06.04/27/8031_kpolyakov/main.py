from math import dist
from turtle import *


def dbscan(r, cur_star, all_stars, cluster):
    neighbours = []
    for star in all_stars.copy():
        if dist(cur_star, star) <= r:
            neighbours.append(star)
            cluster.append(star)
            all_stars.remove(star)
    for neighbour in neighbours:
        dbscan(r, neighbour, all_stars, cluster)
    return cluster


f = open('27-93a.txt')
stars = []
for line in f:
    xy = line.replace(',', '.').split()
    x = float(xy[0])
    y = float(xy[1])
    stars.append([x, y])

clusters = []
for star in stars:
    clusters.append(dbscan(0.4, star, stars, [star]))
print(len(clusters))

m = 30
tracer(0)
cnt = 0
up()
colors = ['red', 'blue', 'green', 'yellow', 'cyan', 'magenta', 'black',
          'indigo', 'violet', 'purple', 'pink', 'brown', 'orange', 'teal']
for cluster in clusters:
    if len(cluster) > 100:
        for star in cluster:
            goto(star[0] * m, star[1] * m)
            dot(4, colors[cnt])
        cnt += 1
done()
