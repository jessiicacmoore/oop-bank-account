from zombie import Zombie

print(Zombie.horde)
Zombie.new_day()
print(Zombie.horde)
zombie1 = Zombie.horde[0]
print(zombie1)
zombie2 = Zombie.horde[1]
print(zombie2)
print(zombie1.encounter())
print(zombie2.encounter())
Zombie.new_day()
print(Zombie.horde)
zombie1 = Zombie.horde[0]
zombie2 = Zombie.horde[1]
print(zombie1.encounter())
print(zombie2.encounter())
