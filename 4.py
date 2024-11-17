import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Список случайных чисел:", numbers)
sorted_numbers = sorted(numbers)
print("Отсортированный список:", sorted_numbers)
print("Минимальное значение:", sorted_numbers[0])
print("Максимальное значение:", sorted_numbers[-1])
total_sum = sum(numbers)
print("Сумма всех чисел в списке:", total_sum)
