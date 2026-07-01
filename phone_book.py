book = {}

while True:
    name = input("Введите имя (пустая строка = выход): ").strip() 
    
    if name == "":
        break  

    phone = input("Введите номер: ").strip()
    book[name] = phone
print("Телефонная книжка: ")
for name, phone in book.items():
    print(f"{name}: {phone}")
    