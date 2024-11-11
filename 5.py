with open("numbers.txt", "w") as file:
    for num in numbers:
        file.write(str(num) + "\n")
with open("numbers.txt", "r") as file:
    data = file.readlines()
    numbers = [int(line.strip()) for line in data]
    avg = sum(numbers) / len(numbers)
    print("Среднее значение чисел:", avg)
file_name = input("Введите имя файла: ")
with open(file_name, "r") as file:
    data = file.readlines()
    # обработка данных
