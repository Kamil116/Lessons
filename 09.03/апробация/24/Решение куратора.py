# Способ 1 (не рекомендуется, на КРАЙНИЙ случай)
f = open('24_20813.txt')
s = f.readline()
# s = s.replace('-', '*')
# # **
# s = s.replace('**', ' ')
# s = s.replace('8', '7').replace('9', '7')
# # *07
# s = s.replace('*07', '*0 7')
# s = s.replace('*00', '*0 0')
# s = s.split()
# maxim = 0
# for cur in s:
#     while cur[0] == '*':
#         cur = cur[1:]
#     while cur[-1] == '*':
#         cur = cur[:-1]
#     if len(cur) > maxim:
#         maxim = len(cur)
# print(maxim)

# Способ 2 (через регулярки, рекомендуется, но нужно тестить!)
from re import finditer

# (пол. число или 0) -* (пол. число или 0)
number = '([1-9][0-9]*|0)'
pattern = f'{number}([-*]{number})*'

max_len = 0
for match in finditer(pattern, s):
    if len(match.group()) > max_len:
        max_len = len(match.group())
print(max_len)
