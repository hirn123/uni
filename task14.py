n = int(input())  # не используется дальше, нужно просто по условию задачи
array = list(map(int, input().split()))
new_array = [array[-1]] + array[:-1]
print(" ".join(map(str, new_array)))
