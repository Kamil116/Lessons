# # Способ 1
# def func(a, b, c1, c2, c3):
#     if a > b:
#         return 0
#     if a == b:
#         return 1
#     if c1 == c2 == c3:
#         if c3 == 1:
#             return func(a * 2, b, 1, 1, 2)
#         else:
#             return func(a + 1, b, 2, 2, 1)
#     else:
#         return func(a + 1, b, c2, c3, 1) + func(a * 2, b, c2, c3, 2)
#
#
# print(func(5, 299, -1, 0, 0))

# Способ 2
def func(a, b, moves):
    if a > b or '1111' in moves or '2222' in moves:
        return 0
    if a == b:
        return 1
    return func(a + 1, b, moves + '1') + func(a * 2, b, moves + '2')


print(func(5, 299, ''))
