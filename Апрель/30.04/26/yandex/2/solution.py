f = open('26_4629_1714058038.txt')
n = int(f.readline())
prices = [int(line) for line in f.readlines()]

# 1. Выгодный вариант
good_prices = sorted(prices, reverse=True)
# print(len(good_prices))  # видим, что товаров 10 тысяч, 25% будет ровно 2500
discounted_price = sum(good_prices[:2500]) * 0.5 + sum(good_prices[2500:])
print(int(discounted_price), end=' ')

# 2. Невыгодный вариант
bad_prices = sorted(prices)
discounted_price = sum(bad_prices[:2500]) * 0.5 + sum(bad_prices[2500:])
print(int(discounted_price))
