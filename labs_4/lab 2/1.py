import json

with open("qwe.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)
    total_age = 0
    count = 0
    for key in json_data:
        json_city = json_data[key]['city']
        if json_city == "Moscow":
            name = json_data[key]['name']
            age = json_data[key]['age']
            print("Имя: ", name)
            print("Возраст: ", age)
            total_age += age
            count += 1
    if count > 0:
        average_age = total_age / count
        average_age1 = int(average_age)
        print("Средний возраст:", average_age1)
