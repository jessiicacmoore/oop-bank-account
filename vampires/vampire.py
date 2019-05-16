class Vampire:

    coven = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = True
        self.drank_blood_today = False

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nIn Coffin: {self.in_coffin}\nDrank Blood Today: {self.drank_blood_today}"

    def __repr__(self):
        return f"{self.name} (Drank Blood: {self.drank_blood_today}  In Coffin: {self.in_coffin})"

    @classmethod
    def create(cls, name, age):
        vampire = Vampire(name, age)
        cls.coven.append(vampire)

    @classmethod
    def sunrise(cls):
        dead_vampires = []
        for vampire in cls.coven:
            if vampire.drank_blood_today is False or vampire.in_coffin is False:
                dead_vampires.append(vampire)

        for vampire in dead_vampires:
            cls.coven.remove(vampire)
            # if vampire.drank_blood_today or vampire.in_coffin:
            #     pass
            # else:
            #     cls.coven.remove(vampire)

    @classmethod
    def sunset(cls):
        for vampire in cls.coven:
            vampire.drank_blood_today = False
            vampire.in_coffin = False

    def drink_blood(self):
        self.drank_blood_today = True

    def go_home(self):
        self.in_coffin = True


Vampire.create("Dracula", 1000)
Vampire.create("Selene", 1500)
Vampire.create("Blade", 2000)
Vampire.create("The Count", 500)

for vampire in Vampire.coven:
    print()
    print(vampire)

print()
print(
    Vampire.coven
)  # [Dracula (Drank Blood: False  In Coffin: True), Selene (Drank Blood: False  In Coffin: True), Blade (Drank Blood: False  In Coffin: True), The Count (Drank Blood: False  In Coffin: True)]

print()
print("----sunset----")
Vampire.sunset()

print()
print(
    Vampire.coven
)  # [Dracula (Drank Blood: False  In Coffin: False), Selene (Drank Blood: False  In Coffin: False), Blade (Drank Blood: False  In Coffin: False), The Count (Drank Blood: False  In Coffin: False)]

print()
print("----drink blood vampire 1 & 3----")
Vampire.coven[0].drink_blood()
Vampire.coven[2].drink_blood()

print()
print(
    Vampire.coven
)  # [Dracula (Drank Blood: True  In Coffin: False), Selene (Drank Blood: False  In Coffin: False), Blade (Drank Blood: True  In Coffin: False), The Count (Drank Blood: False  In Coffin: False)]

print()
print("----go home vampire 3 & 4----")
Vampire.coven[2].go_home()
Vampire.coven[3].go_home()

print()
print(
    Vampire.coven
)  # [Dracula (Drank Blood: True  In Coffin: False), Selene (Drank Blood: False  In Coffin: False), Blade (Drank Blood: True  In Coffin: True), The Count (Drank Blood: False  In Coffin: True)]

print()
print("----sunrise----")
Vampire.sunrise()

print()
print(
    Vampire.coven
)  # [Dracula (Drank Blood: True  In Coffin: False), Blade (Drank Blood: True  In Coffin: True), The Count (Drank Blood: False  In Coffin: True)]

for vampire in Vampire.coven:
    print()
    print(vampire)
