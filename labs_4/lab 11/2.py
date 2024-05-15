class Weapon:
    def __init__(self, name, damage, weapon_group, weapon_type):
        self.name = name
        self.damage = damage
        self.weapon_type = weapon_type
        self.weapon_group = weapon_group

    def attack(self):
        print(
            f"Вы атаковали с помощью оружия {self.name} типа({self.weapon_type}), нанесено {self.damage} урона.")


class Pronged(Weapon):
    def __init__(self):
        super().__init__("Многозубцы", 5, "Клинковое", "Колющее")


class Bayonets(Weapon):
    def __init__(self):
        super().__init__("Штыки граненые", 7, "Клинковое", "Колющее")


class Swords(Weapon):
    def __init__(self):
        super().__init__("Шпаги", 10, "Клинковое", "Колющее")


class Saber(Weapon):
    def __init__(self):
        super().__init__("Сабля", 12, "Клинковое", "Рубящее")


class Scimitar(Weapon):
    def __init__(self):
        super().__init__("Ятаган", 11, "Клинковое", "Колюще-рубящее")


class Digger(Weapon):
    def __init__(self):
        super().__init__("Кинжал", 10, "Клинковое", "Колюще-режущее")


class Club(Weapon):
    def __init__(self):
        super().__init__("Палица", 15, "Неклинковое", "Ударно-раздробляющее")


pl_club = Club()
pl_club.attack()
