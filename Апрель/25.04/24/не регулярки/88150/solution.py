from string import ascii_uppercase


def my_count(pair, string):
    cnt = 0
    for i in range(len(string) - 1):
        if string[i] + string[i + 1] == pair:
            cnt += 1
    return cnt


f = open('24_M5__42njq.txt')
s = f.readlines()
max_str = ''
max_len = 0
for string in s:
    cur = 0
    maxim = 0
    sogl_count = 0
    for i in range(len(string)):
        if string[i] in 'BCDFGHJKLMNPQRSTVWXZ':
            sogl_count += 1
        if sogl_count > 1:
            maxim = max(maxim, cur)
            cur = 0
            sogl_count = 0
        else:
            cur += 1
    if maxim >= max_len:
        max_len = maxim
        max_str = string

all_combinations = [first + second for first in ascii_uppercase for second in ascii_uppercase]

cur = 0
max_comb = None
for combination in all_combinations:
    if my_count(combination, max_str) > cur:
        cur = my_count(combination, max_str)
        max_comb = combination

cur = 0
for string in s:
    cur += my_count(max_comb, string)
print(max_comb, cur)
