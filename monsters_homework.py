class Monster:
    skills = []

    def __init__(self, obj_name):
        self.name = obj_name

    def sleep(self):
        return "zzzzz"

    def eat(self):
        return "nom nom"

    def scare_attack(self):
        return "RAAAHHH"

monster1 = Monster("bob")

print(monster1.sleep())

monster1.skills = "really good at holding breath"

print(monster1.skills)