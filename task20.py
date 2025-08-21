numbers = dict()

start = int(input())
finish = int(input())

if start < finish:
    step = 1
    finish += 1
else:
    step = -1
    finish -= 1

for i in range(start, finish, step):
    numbers[i] = i ** i
print(numbers)
