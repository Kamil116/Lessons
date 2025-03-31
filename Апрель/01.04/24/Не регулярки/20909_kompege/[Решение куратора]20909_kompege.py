f = open('24_20909.txt')
s = f.readline()
s = s.split('AB')
maxim = -1
for i in range(len(s) - 100):
    maxim = max(maxim, sum(map(len, s[i:i + 101])) + 100 * 2 + 2)
print(maxim)

# # Метод двух указателей
# left = 0
# ab_count = 0
# maxim = -1
# for right in range(len(s) - 1):
#     if s[right] + s[right + 1] == 'AB':
#         ab_count += 1
#     while ab_count > 100:
#         maxim = max(maxim, right - left + 1)
#         if s[left] + s[left + 1] == 'AB':
#             ab_count -= 1
#         left += 1
# print(maxim)
