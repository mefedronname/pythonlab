import random

def create_file_with_random_numbers(filename, count=10):
    with open(filename, "w") as file:
        for _ in range(count):
            number = random.randint(1, 100)
            file.write(f"{number}\n")
    print(f"Файл '{filename}' создан и заполнен случайными числами.")

create_file_with_random_numbers("random_numbers.txt")
def calculate_average_from_file(filename):
    with open(filename, "r") as file:
        numbers = [int(line.strip()) for line in file]
        if numbers:
            average = sum(numbers) / len(numbers)
            print(f"Среднее значение чисел в файле '{filename}': {average}")
        else:
            print(f"Файл '{filename}' пуст или не содержит чисел.")

calculate_average_from_file("random_numbers.txt")
def main():
    action = input("Введите 'write' для записи случайных чисел или 'read' для чтения и вычисления среднего: ").strip().lower()
    filename = input("Введите имя файла: ").strip()

    if action == "write":
        count = int(input("Введите количество случайных чисел для записи: "))
        create_file_with_random_numbers(filename, count)
    elif action == "read":
        calculate_average_from_file(filename)
    else:
        print("Неверная команда. Используйте 'write' или 'read'.")

main()
