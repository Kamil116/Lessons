from turtle import *
from math import *

# f = open("27-81a.txt")
f = open("27-81b.txt")


def dbscan(c, r):
    cl = []
    while c:
        cl.append([c.pop(0)])
        for i in cl[-1]:
            for j in c[:]:
                if dist(i, j) < r:
                    cl[-1].append(j)
                    c.remove(j)
    return cl


data = [list(map(float, i.replace(',', '.').split())) for i in f]
a = dbscan(data, 0.44)
t = 0
for i in a:
    i.sort(key=lambda x: x[0])

# color = ['black', 'red', 'green', 'blue', 'purple', 'brown', 'orange']
# tracer(0)
# penup()
# for i in range(len(a)):
#     for j in a[i]:
#         x, y = j
#         goto(x * 60, y * 60)
#         dot(4, color[i])
# done()


sx = sy = 0
for k in range(7):
    ms = 0
    for i in range(len(a[k])):
        q = 0
        x1, y1 = a[k][i]
        for j in range(len(a[k])):
            x2, y2 = a[k][j]
            q += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5 <= 1
        if q >= ms:
            ms = q
            t = a[k][i]
    sx += t[0]
    sy += t[1]

print(int(abs(sx) / 7 * 100_000), int(abs(sy) / 7 * 100_000))
