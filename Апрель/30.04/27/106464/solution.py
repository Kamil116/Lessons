from math import *

f = open('1_A__5wyzi.txt')
f.readline()
a = []
for i in f:
    xym = list(map(float, i.replace(',', '.').split()))
    a.append(xym)


def dbscan(radius, cluster, star, all_stars):
    neighbours = []
    for i in all_stars[:]:
        dst = dist(star[:-1], i[:-1])
        if dst <= radius:
            cluster.append(i)
            all_stars.remove(i)
            neighbours.append(i)
    for d in neighbours:
        dbscan(radius, cluster, d, all_stars)
    return cluster


o = []
clusters = []
while a:
    l = a.pop(0)
    clusters.append(dbscan(0.8, [l], l, a))
for i in clusters:
    if len(i) > 12:
        o.append(i)

b = [[], [], [], []]
for k in range(4):
    while o[k]:
        b[k].append(dbscan(0.3, [], o[k][0], o[k]))

sx = sy = 0
for cluster in b:
    min_per = 1000000000
    tr_sys = None
    for system in cluster:
        if len(system) == 3:
            d1 = dist(system[0][:2], system[1][:2])
            d2 = dist(system[1][:2], system[2][:2])
            d3 = dist(system[0][:2], system[2][:2])
            m1, m2, m3 = system[0][2], system[1][2], system[2][2]
            if d1 <= 0.3 and d2 <= 0.3 and d3 <= 0.3:
                red, yellow = 0, 0
                for m in [m1, m2, m3]:
                    if 0.08 <= m <= 0.6:
                        red += 1
                    if 0.8 <= m <= 1.2:
                        yellow += 1
                if red >= 1 and yellow >= 1:
                    per = d1 + d2 + d3
                    if per < min_per:
                        min_per = per
                        tr_sys = system
    sx += tr_sys[0][0] + tr_sys[1][0] + tr_sys[2][0]
    sy += tr_sys[0][1] + tr_sys[1][1] + tr_sys[2][1]
print(int(sx / 12 * 100), int(sy / 12 * 100))
# Ответ: 164 -1053 825 -53
