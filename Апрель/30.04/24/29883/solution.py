f = open('Задание_11_ДЗ__tcfm.txt')
s = f.readline()
abba = baba = baab = 0
for i in range(len(s) - 3):
    if s[i:i + 4] == 'ABBA':
        abba += 1
    if s[i:i + 4] == 'BABA':
        baba += 1
    if s[i:i + 4] == 'BAAB':
        baab += 1
print(max(abba, baba, baab), end='')
if abba < baba < baab:
    print('ABBA')
