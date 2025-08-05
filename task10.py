# Задание №3 Вводятся целые числа A и B. Гарантируется, что A ≤ B. Выведите все четные числа на заданном отрезке через пробел.
a = int(input())
b = int(input())

even_numbers = []

for i in range(a, b + 1):
    if i % 2 == 0:
        even_numbers.append(str(i))

print(' '.join(even_numbers))
