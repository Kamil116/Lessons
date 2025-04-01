from math import dist
from turtle import *


def dbscan(cur_star, r, all_stars, cluster):
    neighbours = []
    for i in range(len(all_stars)):
        if all_stars[i] != '*' and dist(cur_star, all_stars[i]) <= r:
            neighbours.append(all_stars[i])
            cluster.append(all_stars[i])
            all_stars[i] = '*'
    for neighbour in neighbours:
        dbscan(neighbour, r, all_stars, cluster)
    return cluster


f = open('27-p00a.txt')
stars = [list(map(float, line.replace(',', '.').split())) for line in f.readlines()]
clusters = []
for star in stars:
    if star != '*':
        clusters.append((dbscan(star, 1, stars, [star])))

colors = ['red', 'black', 'purple', 'green', 'yellow', 'blue', 'violet']
cnt = 0
tracer(0)
penup()
for cluster in clusters:
    for star in cluster:
        goto(star[0] * 40, star[1] * 40)
        dot(4, colors[cnt])
    cnt += 1
done()
