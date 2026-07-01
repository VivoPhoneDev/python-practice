def student_info():
    info = {}

    name = input("Представьтесь: ")
    age = int(input(f"Приятно познакомиться {name}!\nСколько тебе лет: "))
    group = input("В какой ты группе: ")
    favourite_subjects = input("2-3 твоих любимых предмета (через запятую): ").split(",")

    info["name"] = name
    info["age"] = age
    info["group"] = group
    info["subjects"] = [s.strip() for s in favourite_subjects]

    return info

def print_student(info):
    print("\nХарактеристика студента")
    print(f"Имя: {info["name"]}")
    print(f"Возраст: {info["age"]}")
    print(f"Группа: {info["group"]}")
    print(f"Любимые предметы: {', '.join(info['subjects'])}")

student = student_info()
print_student(student)