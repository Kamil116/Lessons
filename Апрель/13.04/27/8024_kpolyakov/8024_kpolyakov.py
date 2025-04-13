from math import *

# f = open("27-86a.txt")
f = open("27-86b.txt")


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
a = dbscan(data, 1)
print(len(a))
sx = sy = 0
for k in range(len(a)):
    for i in range(len(a[k])):
        x1, y1 = a[k][i]
        sl = sp = sv = sn = 0
        for j in range(len(a[k])):
            x2, y2 = a[k][j]
            if x2 < x1: sl += 1
            if x2 > x1: sp += 1
            if y2 > y1: sv += 1
            if y2 < y1: sn += 1
        if sl == sp: xmed = a[k][i][0]
        if sv == sn: ymed = a[k][i][1]
    sx += xmed
    sy += ymed

print(int(sx / 3 * 10000), int(sy / 3 * 10000))
