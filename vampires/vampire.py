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
    vampire = Vampire (name, age)
    cls.coven.append(vampire)

  @classmethod
  def sunrise(cls):
    pass

  @classmethod
  def sunset(cls):
    pass

  def drink_blood(self):
    self.drank_blood_today = True

  def go_home(self):
    pass


Vampire.create('Dracula', 1000)
vampire1 = Vampire.coven[0]
print(vampire1)
vampire1.drink_blood()
print(vampire1)

  