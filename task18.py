# Задание №3
# Во входную строку водится последовательность чисел через пробел.
# Для каждого числа выведите слово ”YES” (в отдельной строке), если это число ранее встречалось в последовательности или ”NO”, если не встречалось.
numbers = list(map(int, input().split()))
checked = set()
for num in numbers:
    if num in checked:
        print("YES")
    else:
        print("NO")
    checked.add(num)
