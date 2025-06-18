'''
Задание №2

Дано слово из маленьких латинских букв. Сколько там согласных и гласных букв? Гласными называют буквы «a», «e», «i», «o», «u».

Для решения задачи создайте переменную и в неё положите слово с помощью input()

А также определите количество каждой из этих гласных букв Если какой-то из перечисленных букв нет - Выведите False
'''


word = input('Введите слово из маленьких латинских букв: ')

vowels = ('a', 'e', 'i', 'o', 'u')
letters = ('a', 'e', 'i', 'o', 'u', 'q', 'w', 'r', 'd', 't', 'y', 'p', 's', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
#можно добавить в массив большие буквы чтобы он считал их не как согласные

vowel_count = 0 
consonant_count = 0


if word.isalpha():

    for letters in word:
        if letters in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    
    a = word.count ('a')
    e = word.count ('e')
    i = word.count ('i')
    o = word.count ('o')
    u = word.count ('u')

    print(f"количество гласных = {vowel_count}, количество согласных = {consonant_count}")

    if vowel_count > 0:
        print(f"Количества каждой из гласных: a = {a}, e = {e}, i = {i}, o = {o}, u = {u} ")
    else:
        print('False')

else:
    print("Слово введено неправильно.")
