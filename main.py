from models.human import Human
from models.dog import Dog
from models.cat import Cat
from models.seagull import Seagull

human1 = Human("David", 22, 2)
dog1 = Dog("Simba", 8, 4)
cat1 = Cat("Carl", 4, 4)
seagull1 = Seagull("Jacob", 16, 2)

print(human1.name, human1.age, human1.leg_count)
print(human1.to_string())
print(human1.communicate())
print(human1.can_fly())

