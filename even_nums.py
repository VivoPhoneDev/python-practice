
amount = int(input("Введите кол-во чисел: "))
i = 0
nums = []
num = 0
try:

    def get_even(num, nums):
        if num % 2 == 0:
            nums.append(num)

    for amount in range(amount):
        i += 1
        num = int(input(f"Число № {i}: "))
        get_even(num, nums)
    print(f"Четные числа: {nums}")
except ValueError:
    print ("Ошибка! Вводите только целые числа!")
except Exception as e:
    print(f"Произошла ошибка: {e}")