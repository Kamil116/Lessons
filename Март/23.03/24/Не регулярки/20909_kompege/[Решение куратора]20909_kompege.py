# Способ 1 через split
f = open('24_20909.txt')
s = f.readline()
s = s.split('AB')
maxim = 0
for i in range(len(s) - 100):
    maxim = max(maxim, sum(map(len, s[i:i + 100 + 1])) + 2 + 100 * 2)
print(maxim)

# # Способ 2 через два указателя
# f = open('24_20909.txt')
# s = f.readline()
# # s = 'xxABxxxABxABxxx'
# # xxABxxxABxABxxx
# left = right = count_ab = maxim = 0
# for right in range(len(s) - 1):
#     if s[right:right + 2] == 'AB':
#         count_ab += 1
#     while count_ab == 101:
#         maxim = max(maxim, right - left + 1)
#         if s[left:left + 2] == 'AB':
#             count_ab -= 1
#         left += 1
# print(maxim)
