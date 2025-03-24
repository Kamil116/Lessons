# # Решение для файла А
# f = open('27-p00a.txt')
# clusters = [[] for _ in range(2)]
# for line in f:
#     star = list(map(float, line.replace(',', '.').split()))
#     x = star[0]
#     if x > 1:
#         clusters[0].append(star)
#     else:
#         clusters[1].append(star)
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

# # Решение для файла Б
f = open('27-p00b.txt')
clusters = [[] for _ in range(3)]
for line in f:
    star = list(map(float, line.replace(',', '.').split()))
    x, y = star
    if y < 4 and x < 3:
        clusters[0].append(star)
    elif y > 6 and 2 < x < 5:
        clusters[1].append(star)
    elif x > 5:  # можно было использовать else
        clusters[2].append(star)

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
