print("Максимальная масса, которую может выдержать одна лодка равна:")
m = int(input())

print("Количество рыбаков равно:")
n = int(input())

weights = []

print("Введите массу каждого рыбака:")

for i in range(n):
    fishmen_weight = int(input())
    weights.append(fishmen_weight)
weights.sort()
left = 0
right = n - 1
boat_count = 0
while left <= right:
    if weights[left] + weights[right] <= m:
        left += 1
    right -= 1
    boat_count += 1
print(f"Потребуется, {boat_count} лодки.")
