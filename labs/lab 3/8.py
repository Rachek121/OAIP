word = input("Введите слово:")
shortest_word = word
while word != "стоп":
    if len(word) < len(shortest_word):
        shortest_word = word
        word = input("Введите слово:")
        print("Самое короткое слово:", shortest_word)
