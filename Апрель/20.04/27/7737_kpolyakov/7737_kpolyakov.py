from math import dist


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


f = open('27-62a.txt')
stars = [list(map(float, line.replace(',', '.').split())) for line in f.readlines()]
clusters = []
for star in stars:
    if star != '*':
        cluster = dbscan(star, 1, stars, [])
        if len(cluster) > 100:
            clusters.append(cluster)

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
print(int(sx / len(clusters) * 100_000), int(sy / len(clusters) * 100_000))
