# Решение Полины
f = open('26-152.txt')
n = int(f.readline())
goods = []
for i in range(n):
    goods.append(list(map(int, f.readline().split())))

# [[100], [200], [100], [300]]
new_goods = []
for i in range(len(goods)):
    good_id = goods[i][0]
    done = [good[0] for good in new_goods]
    # done = list(map(lambda x: x[0], new_goods))
    if good_id in done:
        continue  # i -> i + 1

    sold = 0
    rem = 0
    for j in range(len(goods)):
        if goods[j][0] == good_id:
            if goods[j][2] == 1:
                rem += 1
            elif goods[j][2] == 0:
                sold += 1
    new_goods.append([good_id, sold, rem, goods[i][1]])
s = 0
c = 0
for g in range(len(new_goods)):
    s += new_goods[g][-1]
    c += 1
sr = s / c
dr = []
for k in range(len(new_goods)):
    if new_goods[k][-1] > sr:
        dr.append(new_goods[k])

dr.sort(key=lambda x: (-x[1], -x[-1], x[2]))
print(dr)

# 43656 36
