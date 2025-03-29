from math import dist
from turtle import *


def draw_clusters(clusters):
    tracer(0)
    penup()
    colors = ['red', 'blue', 'purple']
    for i in range(len(clusters)):
        for star in clusters[i]:
            goto(star[0] * 8, star[1] * 12)
            dot(5, colors[i])
    update()
    mainloop()


def dbscan(cur_star, r, all_stars, cluster):
    neighbours = []
    for i in range(len(all_stars)):
        if all_stars[i] != '*' and dist(cur_star[:2], all_stars[i][:2]) <= r:
            neighbours.append(all_stars[i])
            cluster.append(all_stars[i])
            all_stars[i] = '*'
    for star in neighbours:
        dbscan(star, r, all_stars, cluster)
    return cluster


# f = open('4_A__5wzaw.txt')
f = open('4_B__5wzaz.txt')
f.readline()
# r = 0.7
# t = 0.11
r = 0.6
t = 0.05
stars = [list(map(float, line.replace(',', '.').split())) for line in f.readlines()]

clusters = []
for star in stars:
    if star != '*':
        clusters.append(dbscan(star, r, stars, []))

normal_clusters = []
for cluster in clusters:
    if len(cluster) > 10:
        normal_clusters.append(cluster)

# draw_clusters(normal_clusters)
px = []
py = []
for cluster in normal_clusters:
    minim_sum_mass = 10 ** 10
    min_system = None
    systems = []
    for star in cluster:
        if star != '*':
            systems.append(dbscan(star, t, cluster, []))
    for system in systems:
        if len(system) == 3:
            first_star_coords, second_star_coords, third_star_coords = system[0][:2], system[1][:2], system[2][:2]
            if (dist(first_star_coords, second_star_coords) <= t
                    and dist(second_star_coords, third_star_coords) <= t
                    and dist(first_star_coords, third_star_coords) <= t):
                masses = [system[0][2], system[1][2], system[2][2]]
                black_star = [mass for mass in masses if mass < -2.7]
                neutron_star = [mass for mass in masses if -2.7 <= mass <= 0]
                if len(black_star) >= 1 and len(neutron_star) >= 1:
                    if sum(masses) < minim_sum_mass:
                        minim_sum_mass = sum(masses)
                        min_system = system
    px += [star[0] for star in min_system]
    py += [star[1] for star in min_system]
print(int(sum(px) / len(px) * 500), int(sum(py) / len(py) * 500))
