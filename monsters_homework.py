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

    def addskill(self, obj_skill):
        self.skills.append(obj_skill)

