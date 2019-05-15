class Vampire:

    coven = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = True
        self.drank_blood_today = False

    def __str__(self):
        return f"Name: {self.name}\nAge: {self.age}\nIn Coffin: {self.in_coffin}\nDrank Blood Today: {self.drank_blood_today}"

    @classmethod
    def create(cls, name, age):
        vampire = Vampire(name, age)
        cls.coven.append(vampire)

    @classmethod
    def sunrise(cls):
        for vampire in cls.coven:
            if not vampire.drank_blood_today or not vampire.in_coffin:
                cls.coven.remove(vampire)

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

print(Vampire.coven[0])
print(Vampire.coven[1])
print(Vampire.coven[2])
print(len(Vampire.coven))

print("---drink blood vampire 1 + 2---")
Vampire.coven[0].drink_blood()
Vampire.coven[1].drink_blood()

print(Vampire.coven[0])
print(Vampire.coven[1])
print(Vampire.coven[2])
print(len(Vampire.coven))

print("---sunrise---")
Vampire.sunrise()
print(len(Vampire.coven))
print(Vampire.coven)

print("---sunset---")
Vampire.sunset()
print(Vampire.coven[0])
print(Vampire.coven[1])
print(len(Vampire.coven))

print("---drink blood vampire 1 + 2---")
Vampire.coven[0].drink_blood()
Vampire.coven[1].drink_blood()

print(Vampire.coven[0])
print(Vampire.coven[1])

print("---go home vampire 1---")
Vampire.coven[0].go_home()

print(Vampire.coven[0])
print(Vampire.coven[1])

print("---sunrise---")
Vampire.sunrise()
print(len(Vampire.coven))
print(Vampire.coven)
