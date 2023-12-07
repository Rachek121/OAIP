import random
words = ['Да', 'Нет', 'Скорее всего да', 'Скорее всего нет', 'Возможно','Имеются перспективы', 'Вопрос задан неверно']
word = random.choice(words)
question = input('Введите воспрос: ')
check = question.replace('?', '')
print('Ваш вопрос==>', check, '\nОтвет:', word)
