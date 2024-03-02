def count_word(s):
    vowels = "aeiouyAEIOUYауоыиэяюёеАУОЫИЭЯЮЁЕ"
    if len(s) == 0:
        return 0
    else:
        if s[0] in vowels:
            return 1 + count_word(s[1:])
        else:
            return count_word(s[1:])


input_string = input("Введите строку: ")
result = count_word(input_string)
print(f"Количество гласных букв в строке: {result}")
