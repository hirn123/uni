# Задание №2 Вводится натуральное число X. Подсчитайте количество натуральных делителей числа X (включая 1 и само число). x ≤ 2e9 (2 миллиарда)
x = int(input())


if x >= 2 * 10 ** 9:
    print("too large number")
else:
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
print(count)
