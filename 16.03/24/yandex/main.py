# Решение Егора
f = open("../files/24.txt").readline().replace('878', '*').split('78')
for i in range(len(f)):
    f[i] = f[i].replace('*', '878')
lmax = 0
for i in range(len(f) - 1):
    l1 = l2 = 0
    s1 = f[i]
    s2 = f[i + 1]
    d1 = d2 = ''
    for k in range(79, 10 ** 10):
        d2 = d2 + str(k)
        if s2[:len(d2)] == d2:
            l2 = len(d2)
        else:
            break
    for k in range(77, -1, -1):
        d1 = str(k) + d1
        if s1[-len(d1):] == d1:
            l1 = len(d1)
        else:
            break
    lmax = max(lmax, l1 + l2 + 2)
print(lmax)
