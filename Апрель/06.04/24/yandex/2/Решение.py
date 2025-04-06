# Решение Полины
f = open('24_1.txt')
s = f.readline()
c = 0
for i in range(len(s) - 2):
    if s[i] in 'ABC' and s[i + 1] in 'CDE' and s[i + 2] in 'BCDF':
        if len(s[i:i + 3]) == len(set(s[i:i + 3])):
            c += 1
print(c)

# # Решение Кати
# f = open('24_1.txt').readline()
# k = 0
# for i in range(len(f) - 2):
#     if f[i] != f[i + 1] and f[i] != f[i + 2] and f[i + 1] != f[i + 2]:
#         if f[i] == 'A' or f[i] == 'B' or f[i] == 'C':
#             if (f[i + 1] == 'C' or f[i + 1] == 'D' or f[i + 1] == 'E'):
#                 if f[i + 2] == 'C' or f[i + 2] == 'D' or f[i + 2] == 'B' or f[i + 2] == 'F':
#                     k += 1
# print(k)
