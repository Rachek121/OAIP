phone_number = input("Введите номер телефона: ")
if not all(char.isdigit() or char == '+' for char in phone_number):
    print('Неправильный номер телефона!')
else:
    print('Авторизация успешна!')
