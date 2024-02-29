def count_vowels(s):
    vowels = "aeiouyAEIOUYауоыиэяюёе"
    if len(s) == 0:
        return 0
    else:
        if s[0] in vowels:
            return 1 + count_vowels(s[1:])
        else:
            return count_vowels(s[1:])

input_string = input("Введите строку: ")
result = count_vowels(input_string)
print(f"Количество гласных букв в строке: {result}")
