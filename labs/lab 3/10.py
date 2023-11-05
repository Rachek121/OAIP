words = []
while True:
    word = input("Введите слово\n>>>")
    if word == "стоп":
        break
    words.append(word)
    text = ' '.join(words)
    sentences = text.split('!')
    for sentence in sentences:
        print(sentence.strip())
