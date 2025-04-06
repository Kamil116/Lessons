from turtle import *

from math import dist

f = open('27-92b.txt')
stars = []
for line in f.readlines():
    xy = line.replace(',', '.').split()
    x = float(xy[0])
    y = float(xy[1])
    stars.append([x, y])


# stars = [list(map(float, line.replace(',', '.').split())) for line in f.readlines()]


def dbscan(r, cur_star, all_stars, cluster):
    neighbours = []
    all_stars_copy = all_stars.copy()
    for star in all_stars_copy:
        if dist(cur_star, star) <= r:
            neighbours.append(star)
            cluster.append(star)
            all_stars.remove(star)
    for neighbour in neighbours:
        dbscan(r, neighbour, all_stars, cluster)
    return cluster


clusters = []
for star in stars:
    clusters.append(dbscan(0.4, star, stars, [star]))

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'lightskyblue', 'violet', 'grey']
cnt = 0
tracer(0)
m = 20
penup()
for cluster in clusters:
    for star in cluster:
        goto(star[0] * m, star[1] * m)
        dot(4, colors[cnt])
    cnt += 1
done()
