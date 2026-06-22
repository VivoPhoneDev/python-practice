numbers = []
i = 0 

print("Введите числа (просто нажмите Enter, чтобы закончить)")

while True:
    i += 1
    user_input = input(f"Число №{i}")
    if user_input.strip() == "":
        break
    try:
        num = int(user_input)
        numbers.append(num)
    except ValueError:
        print("Ошибка: Ведите число!")
if not numbers:
    print("Среднее: 0")
else:
    total = 0
    for num in numbers:
        total += num
    
    average = total / len(numbers)
    print(f"Среднее: {average}")