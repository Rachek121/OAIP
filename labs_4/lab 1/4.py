with open("lines.txt", "r") as file:
    words = file.read().split()
    max_word_len = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_word_len]
    print("максимальная длина: ", max_word_len)
    print("Слова максимум: ")
    for word in longest_words:
        print(word)
