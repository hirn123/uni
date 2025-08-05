# Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.
n = int(input())
zero_count = 0
for i in range(n):
    num = int(input())
    if num == 0:
        zero_count += 1
print(zero_count)
