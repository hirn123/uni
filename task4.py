number = int(input("Введите пятизначное число: "))
a = (number // 10000) #десятки тысяч
b = (number // 1000) % 10 #тысячи
c = (number // 100) % 10 #сотни
d = (number // 10) % 10 #десятки
e = number % 10 #единицы
result = (d ** e) * c // (a - b)
print(result)