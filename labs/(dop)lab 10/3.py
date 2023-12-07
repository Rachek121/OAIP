import random
words = ['яблоко']
word = random.choice(words)
hidden_word = [''] * len(word)
attempts = 5
print("Добро пожаловать в игру 'Угадай слово'!")
while '' in hidden_word and attempts > 0:
    print(' '.join(hidden_word))
    guess = input("Угадайте букву: ")
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess
        print("Поздравляю, вы угадали букву!")
    else:
        attempts -= 1
        print("Увы, такой буквы в слове нет. У вас осталось {} попыток.".format(attempts))
if '_' not in hidden_word:
    print(' '.join(hidden_word))
    print("Поздравляю, вы угадали слово '{}'!".format(word))
else:
    print("Увы, вы проиграли. Загаданное слово было '{}'.".format(word))
