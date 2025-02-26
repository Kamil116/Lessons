f = open('8__1vq2j.txt')
s = f.readline()

"""
Решение 1
s = s.split('AE')
print(max(map(len, s)) + 2)
"""

# Решение 2
# cur = 0
# maxim = 0
# for i in range(len(s) - 1):
#     if s[i] + s[i + 1] == 'AE':
#         maxim = max(cur + 1, maxim)
#         cur = 0
#     else:
#         cur += 1
#         maxim = max(cur, maxim)
# print(maxim)
