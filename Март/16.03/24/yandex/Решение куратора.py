# Ссылка на задачу:
# https://education.yandex.ru/ege/task/14f0894b-7da9-48ac-b096-d94b9066c0d8

f = open('../files/24.txt')
s = f.readline()
s = s.replace('878', '*')
s = s.split('78')
for i in range(len(s)):
    s[i] = s[i].replace('*', '878')
maxim = -1
for i in range(len(s) - 1):
    left_str = s[i]
    right_str = s[i + 1]
    cur = 79
    cur_ans = 0
    for j in range(0, len(right_str), 2):
        if right_str[j:j + 2] == str(cur):
            cur_ans += 2
            cur += 1
            if cur == 100:
                for k in range(j + 2, len(right_str), 3):
                    if right_str[k:k + 3] == str(cur):
                        cur_ans += 3
                        cur += 1
                    else:
                        break
                break
        else:
            break
    cur = 77
    for k in range(len(left_str), -1, -2):
        if left_str[k - 2: k] == str(cur):
            cur -= 1
            cur_ans += 2
        else:
            break
    if cur_ans + 2 > maxim:
        maxim = cur_ans + 2
print(maxim)
# 77
