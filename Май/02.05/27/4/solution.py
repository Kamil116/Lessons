from math import dist
from turtle import *

f = open('27_1_A.txt')
clusters = [[] for _ in range(3)]
for line in f.readlines():
    x, y = map(float, line.replace(',', '.').split())
    if x < 17 and y > 10:
        clusters[0].append([x, y])
    elif y < 10:
        clusters[1].append([x, y])
    else:
        clusters[2].append([x, y])

minim_points = 10 ** 10
maxim_points = -10 ** 10
minim_points_antricentroid = None
maxim_points_antricentroid = None
for cluster in clusters:
    maxim = -100
    anticentr = None
    for anticentroid in cluster:
        ls = 0
        for point in cluster:
            ls += dist(point, anticentroid)
        if ls > maxim:
            maxim = ls
            anticentr = anticentroid
    if len(cluster) < minim_points:
        minim_points = len(cluster)
        minim_points_antricentroid = anticentr
    if len(cluster) > maxim_points:
        maxim_points = len(cluster)
        maxim_points_antricentroid = anticentr
print(int(minim_points_antricentroid[0] * 10_000), end=' ')
print(int(maxim_points_antricentroid[1] * 10_000))
