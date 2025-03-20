def sum_cifr(n):
    summa = 0
    # 135
    # 1. 5, n = 13
    # 2. 5 + 3, n = 1
    # 3. 5 + 3 + 1, n = 0
    # % 10 достаёт последнюю цифру
    # // 10 убирает последнюю цифру
    while n > 0:
        summa += n % 10
        n //= 10
    return summa


f = open('17-428.txt')
numbers = [int(x) for x in f.readlines()]

kr_531 = 0
for number in numbers:
    if number % 531 == 0:
        kr_531 += 1

kr_773 = 0
for number in numbers:
    if number % 773 == 0:
        kr_773 += 1

cnt = 0
total_sum = 0
for i in range(len(numbers) - 2):
    x, y, z = numbers[i], numbers[i + 1], numbers[i + 2]

    # сколько есть трёхзначных чисел в тройке
    first = int(100 <= x <= 999) + int(100 <= y <= 999) + int(100 <= z <= 999)
    second = int(sum_cifr(x) == kr_531) + int(sum_cifr(y) == kr_531) + int(sum_cifr(z) == kr_531)
    third = int(sum_cifr(x) == kr_773) + int(sum_cifr(y) == kr_773) + int(sum_cifr(z) == kr_773)
    if first >= 1 and second <= 1 and third >= 2:
        cnt += 1
        total_sum += x + y + z
print(cnt, total_sum // cnt)
