import json

data = {
    "Фамилия": input("Введите фамилию: "),
    "Имя": input("Введите имя: "),
    "Отчество": input("Введите отчество: "),
    "Телефон": input("Введите номер телефона: "),
    "Год рождения": int(input("Введите год рождения: ")),
    "Город рождения": input("Введите город рождения: "),
    "Место учёбы": input("Введите место учебы: ")
}

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    print("Файл data.json успешно создан")
