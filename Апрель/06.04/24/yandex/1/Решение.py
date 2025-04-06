# # Решение Полины
# f = open('24.txt')
# s = f.readline()
# s = s.replace('4', 'a').replace('3', 'e').replace('yandex', '*')
# h = '*'
# while h in s:
#     h += '*'
# h = h[:-1]
# if h + 'yande' in s:
#     h = h + 'yande'
# elif h + 'yand' in s:
#     h = h + 'yand'
# elif h + 'yan' in s:
#     h = h + 'yan'
# elif h + 'ya' in s:
#     h = h + 'ya'
# elif h + 'y' in s:
#     h = h + 'y'
# print(len(h) * 6)  # 1 звёздочка = yandex, кроме звёзд ничего нет, конец полный

# Решение Амины
f = open('24.txt')
s = f.readline()
s = s.replace('4', 'a').replace('3', 'e')
for i in range(len(s)):
    if 'yandex' * i in s:
        print(i)
