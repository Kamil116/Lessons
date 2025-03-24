from re import *

f = open('../files/24-314.txt')
s = f.readline()

num = '(?:[1-5][0-5]*|0)'
pattern = f'{num}(?:[+*]{num})*'


def func(s):
    new_s = ''
    num = ''
    for i in range(len(s)):
        if s[i] != '*' and s[i] != '+':
            num += s[i]
        else:
            new_s += str(int(num, 6))
            new_s += s[i]
            num = ''
    if s[-1] != '*' and s[-1] != '+':
        new_s += str(int(num, 6))
    return new_s


print(eval(func(max(findall(pattern, s), key=len))))
