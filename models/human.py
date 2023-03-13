from models.animal import Animal


class Human(Animal):

    def __init__(self, name, age, leg_count):
        super().__init__(name, age, leg_count)

    def to_string(self):
        d1 = dict()
        d1['Name'] = self.name
        d1['Age'] = self.age
        d1['Leg_Count'] = self.leg_count
        return d1

    def communicate(self):
        print("I am human,so i can talk")

    def can_fly(self):
        return False
