from math import dist
from turtle import *


def dbscan(r, cur_star, all_stars, cluster):
    neighbours = []
    for i in range(len(all_stars)):
        if all_stars[i] != '*' and dist(cur_star, all_stars[i]) <= r:
            neighbours.append(all_stars[i])
            cluster.append(all_stars[i])
            all_stars[i] = '*'
    for neighbour in neighbours:
        dbscan(r, neighbour, all_stars, cluster)
    return cluster


f = open('27-62a.txt')
stars = [list(map(float, line.replace(',', '.').split())) for line in f.readlines()]

clusters = []
for star in stars:
    if star != '*':
        cluster = dbscan(1, star, stars, [])
        if len(cluster) > 100:
            clusters.append(cluster)

tracer(0)
colors = ['black', 'blue', 'red', 'green', 'orange']
pu()
m = 30
ind = 0
for cluster in clusters:
    for star in cluster:
        goto(star[0] * m, star[1] * m)
        dot(3, colors[ind])
    ind += 1
done()
