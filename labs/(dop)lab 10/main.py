import random
all_characters = 'abcdefghijklnopqrstuvwxyz'
a2ll_characters = '1234567890'
a3ll_characters = '!?%№*+=$#@{}[]()^/|.,'
a4ll_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
long = input('длина пароля?' + "\n")
long = int(long)
password = ''
for i in range(long):
    password += random.choice(all_characters)
    password += random.choice(a2ll_characters)
    password += random.choice(a3ll_characters)
    password += random.choice(a4ll_characters)
    print(password)
