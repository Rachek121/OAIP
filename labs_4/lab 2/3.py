import json

with open("data.json", "r", encoding='utf-8') as file:
    json_data = json.load(file)
print("Данные:")
for key, value in json_data.items():
    print(f"{key}: {value}")

edit_key = input("Введите ключ, для его изменения: ")
if edit_key in json_data:
    new_value = input(f"Новое значения ключа '{edit_key}': ")
    json_data[edit_key] = new_value

    with open("data.json", "w", encoding="utf-8") as json.file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)
