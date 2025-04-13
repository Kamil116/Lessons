from turtle import *
from math import *

# f = open("27-68a.txt")
f = open("27-68b.txt")


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
a = [i for i in dbscan(data, 0.2) if len(i) >= 30]
print(len(a))

color = ['black', 'red', 'green', 'blue', 'purple', 'brown', 'orange']
tracer(0)
penup()
for i in range(len(a)):
    for j in a[i]:
        x, y = j
        goto(x * 60, y * 60)
        dot(4, color[i])
done()

sx = sy = 0
for k in range(len(a)):
    ms = float('inf')
    for i in range(len(a[k])):
        d = 0
        x1, y1 = a[k][i]
        for j in range(len(a[k])):
            x2, y2 = a[k][j]
            d += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if d < ms:
            ms = d
            t = a[k][i]
    sx += t[0]
    sy += t[1]

print(int(sx / 4 * 10000), int(sy / 4 * 10000))
