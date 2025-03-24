from re import findall

f = open('24-278.txt')
s = f.readline()

maxim = 0
for chet in '02468':
    pattern = f'{chet}[KNLF]+{chet}'
    res = findall(pattern, s)
    maxim = max(maxim, len(max(res, key=len)))
print(maxim - 2)
# -2, потому что убираем по цифре слева и справа
