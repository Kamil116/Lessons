from math import ceil

f = open('26_19599.txt')
n = int(f.readline())
gladiators = []
for line in f.readlines():
    code, hp, friend_num, enemy_1, enemy_2, enemy_3 = map(int, line.split())
    gladiators.append([code - 1, hp, friend_num - 1, [enemy_1 - 1, enemy_2 - 1, enemy_3 - 1]])
gladiators.sort()

cnt_alive = n
died_cnt = 0
for i in range(len(gladiators)):
    if gladiators[i][1] > 0:
        # помощь союзнику
        if gladiators[gladiators[i][2]][1] > 0:
            gladiators[gladiators[i][2]][1] += gladiators[i][1]
        # сражение
        for j in range(len(gladiators[i][3])):
            if gladiators[gladiators[i][3][j]][1] > 0 and gladiators[i][1] > 0:
                if gladiators[gladiators[i][3][j]][1] > gladiators[i][1]:
                    gladiators[i][1] = 0
                    gladiators[gladiators[i][3][j]][1] = ceil(
                        gladiators[gladiators[i][3][j]][1] * (2 / 3))
                    died_cnt += 1
                    cnt_alive -= 1
                elif gladiators[gladiators[i][3][j]][1] < gladiators[i][1]:
                    gladiators[i][1] = ceil(gladiators[i][1] * (2 / 3))
                    gladiators[gladiators[i][3][j]][1] = 0
                    died_cnt += 1
                    cnt_alive -= 1
                else:
                    gladiators[i][1] = 0
                    gladiators[gladiators[i][3][j]][1] = 0
                    died_cnt += 2
                    cnt_alive -= 2

alive = list(filter(lambda x: x[1] > 0, gladiators))
assert died_cnt == n - len(alive)
print(died_cnt, max(map(lambda x: x[1], alive)))
