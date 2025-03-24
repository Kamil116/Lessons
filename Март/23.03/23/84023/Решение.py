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
# строка moves хранит ходы, где
# 1 - увеличить на 1
# 2 - умножить на 2
def func(a, b, moves):
    # перешагнули за финиш, либо какая-то команда повторяется подряд 4 раза
    if a > b or '1111' in moves or '2222' in moves:
        return 0
    if a == b:
        return 1
    return func(a + 1, b, moves + '1') + func(a * 2, b, moves + '2')


# 5 -> 6 '1'
# 5 -> 6 -> 12 -> 24 -> 48 '1222'
print(func(5, 299, ''))
