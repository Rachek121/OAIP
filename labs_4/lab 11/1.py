class Widget:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Создан виджет шириной {self.width} и высотой {self.height}.")


class Label(Widget):
    def __init__(self, text, width, height):
        super().__init__(width, height)
        self.text = text

    def draw(self):
        super().draw()
        print(f"Текст: {self.text}.")


class LineEdit(Widget):
    def __init__(self, width, height):
        super().__init__(width, height)

    def draw(self):
        super().draw()
        print("Создано поле для ввода линии текста.")


class TextEdit(Widget):
    def __init__(self, width, height):
        super().__init__(width, height)

    def draw(self):
        super().draw()
        print("Создано поле для ввода  текста.")


class Button(Widget):
    def __init__(self, text, width, height):
        super().__init__(width, height)
        self.text = text

    def draw(self):
        super().draw()
        print(f"Текст на кнопке: {self.text}.")


class CheckBox(Widget):
    def __init__(self, text, width, height):
        super().__init__(width, height)
        self.text = text

    def draw(self):
        super().draw()
        print(f"флаг: {self.text}.")



label = Label("Привет, мир!", 100, 30)
line_edit = LineEdit(150, 30)
text_edit = TextEdit(200, 100)
button = Button("Нажми меня", 80, 40)
checkbox = CheckBox("Правильный", 120, 20)

label.draw()
print()
line_edit.draw()
print()
text_edit.draw()
print()
button.draw()
print()
checkbox.draw()
