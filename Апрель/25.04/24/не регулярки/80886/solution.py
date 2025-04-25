f = open('24_18__3b9tx.txt')
s = f.readline()
ans = 0
for i in range(len(s)):
    f_count, l_count = 0, 0
    for j in range(i, len(s)):
        if s[j] == 'F':
            f_count += 1
        if s[j] == 'L':
            l_count += 1
        if f_count > 3 or l_count > 3:
            break
        ans = max(ans, j - i + 1)
print(ans)

# # Два указателя
# f = open('24_18__3b9tx.txt')
# s = f.readline()
# left = 0
# ans = 0
# f_count = 0
# l_count = 0
# for right in range(len(s)):
#     if s[right] == 'F':
#         f_count += 1
#     if s[right] == 'L':
#         l_count += 1
#     while f_count > 3 or l_count > 3:
#         if s[left] == 'F':
#             f_count -= 1
#         if s[left] == 'L':
#             l_count -= 1
#         left += 1
#     if f_count <= 3 and l_count <= 3:
#         ans = max(ans, right - left + 1)
# print(ans)
