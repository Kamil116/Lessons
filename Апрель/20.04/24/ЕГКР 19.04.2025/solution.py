f = open('24.txt')
s = f.readline().split('RSQ')
# s = 'xxSxSxxxSxxxSx'
# ['xx', 'x', 'xxx', 'xxx', 'x']
# s[1] + s[2] - 3 штуки
# s[1:3] s[i:i + 2]
minim = 10000
for i in range(len(s) - 129):
    if s[i + 129] == '':
        minim = min(minim, sum(map(len, s[i: i + 129])) + 3 * 130 + 1)
    else:
        ind = 0
        j = i + 129
        letter = s[i + 129][ind]
        while letter == 'Q':
            ind += 1
            if ind == len(s[i + 129]):
                break
            letter = s[i + 129][ind]
        minim = min(minim, sum(map(len, s[i: i + 129])) + 3 * 130 + ind + 1)
print(minim)
