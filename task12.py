# Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один. Выведите измененную строку.
word = input()
splitted_word = word.split()
result = ' '.join(splitted_word)
print(result)
