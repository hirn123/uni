print("Введите стороны прямоугольника через пробел (Например: 2.5 5)")
a, b = map(float, input().split())
p = 2 * (a + b)
s = (a * b)
print("Периметр равен", p, "Площадь равна", s)