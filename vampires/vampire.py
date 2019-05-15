class Vampire:

  coven = []

  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.in_coffin = True

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
    pass

  def go_home(self):
    pass

  