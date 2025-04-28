def is_prime(x):
    """
    Функция для выяснения, простое ли число.
    True -> простое, False -> составное
    """
    if x == 1:  # 1 - не простое число
        return False
    for j in range(2, int(x ** 0.5) + 1):  # эффективный перебор до корня
        if x % j == 0:  # нашёлся хотя бы 1 делитель
            return False
    return True


cnt = 0  # количество
minim = 100000000  # минимальное число
for n in range(173225, 217437 + 1):
    for k in range(2, int(n ** 0.5) + 1):  # перебор потеницальных делителей
        if n % k == 0:  # если это действительно делитель
            if is_prime(n // k) and is_prime(k) and k != (n // k) and (n // k) % 10 == k % 10:
                cnt += 1
                minim = min(minim, n)
                break
print(cnt, minim, sep='')
