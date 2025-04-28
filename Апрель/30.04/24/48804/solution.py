f = open('9__19jzs.txt')
s = '_' + f.readline()
new_str = ''
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        new_str = new_str + s[i + 1]
print(sum([int(el) for el in new_str]))
