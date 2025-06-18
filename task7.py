'''
Задание №3

Два инвестора - Майкл и Иван хотят вложиться в стартап. 
Фаундеры сказали, что минимальная сумма инвестиций - X долларов, больше инвестировать можно сколько угодно. 
У Майкла A долларов, у Ивана B долларов. 
Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.
'''


invest = int(input('Минимальная сумма инвестиций равна: '))
mike = int(input('Долларов у Майка: '))
ivan = int(input('Долларов у Ивана: '))
share = mike + ivan

if invest <= mike and invest <= ivan:
    print(2)
else:
    if invest <= mike and invest > ivan:
        print("Mike")
    elif invest <= ivan and invest > mike:
        print("Ivan")
    elif invest <= share:
        print(1)
    else:
        print(0) 
    
