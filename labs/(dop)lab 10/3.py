import random
words = ['яблоко']
word = random.choice(words)
hidden_word = [''] * len(word)
while '' in hidden_word:
    print(' '.join(hidden_word))
    guess = input("Угадайте букву: ")
    for i in range(len(word)):
        if word[i] == guess:
            hidden_word[i] = guess
print(' '.join(hidden_word))
print("Поздравляю, вы угадали слово '{}'!".format(word))
