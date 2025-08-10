# Задание №2
# Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый.
# Все числа каждого списка находятся на отдельной строке.
# Выведите, сколько чисел содержится одновременно как в первом списке, так и во втором.

print("Введите количество чисел в первом списке:")
cycle_number_1 = int(input())

number_list_1 = []

print("Введите числа в первом списке:")

for i in range(cycle_number_1):
    number = int(input())
    number_list_1.append(number)
unique_numbers_1 = set(number_list_1)


print("Введите количество чисел во втором списке:")

cycle_number_2 = int(input())

number_list_2 = []

print("Введите числа во втором списке:")
for i in range(cycle_number_2):
    number = int(input())
    number_list_2.append(number)
unique_numbers_2 = set(number_list_2)

print(unique_numbers_1.union(unique_numbers_2))
