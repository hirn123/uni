def factorial(number):
    if number > 0:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
        return fact
    else:
        return ("number must be > 0")


num = int(input("Введите число: "))
first_fact = factorial(num)
print(first_fact)


fact_list = []
for i in range(first_fact, 0, -1):
    fact_list.append(factorial(i))
print(fact_list)
