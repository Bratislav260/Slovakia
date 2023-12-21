class Mainhero:
    people = 'people'

    def __init__(self, name, nikename, ras, superpower, health_points, damage, dexter, regene, catchphrase):
        self.name = name
        self.nikename = nikename
        self.ras = ras
        self.superpower = superpower
        self.health_points = health_points
        self.damage = damage
        self.dexter = dexter
        self.regene = regene
        self.catchphrase = catchphrase
        self.haraktikistic = [self.name, self.nikename, self.ras, self.superpower,
                              self.health_points, self.damage, self.dexter, self.regene, self.catchphrase]

    def __str__(self):
        return "Имя героя: {},\nРаса: {},\nПрозвище: {},\nУльта: {},\nЗдоровье: {},\nУрон: {},\nЛовкость: {}, \nРегенарация: {},\nФраза: {}"\
            .format(self.name, self.nikename, self.ras, self.superpower, self.health_points,
                    self.damage, self.dexter, self.regene, self.catchphrase)


class Ork_hero(Mainhero):
    fly = False
    boevoy_duh = True

    def __init__(self, name, nikename, ras, superpower, health_points, damage, dexter, regene, catchphrase):
        Mainhero.__init__(self, name, nikename, ras, superpower,
                          health_points, damage, dexter, regene, catchphrase)

        self.buffed_damage = int(damage+(damage*0.2))

    def newstr(self):
        return super().__str__().replace(str(self.damage), str(self.buffed_damage))

    def Yrost_berserka(): ...


class Human_hero(Mainhero):
    fly = False

    def __init__(self, name, nikename, ras, superpower, health_points, damage, dexter, regene, catchphrase):
        Mainhero.__init__(self, name, nikename, ras, superpower,
                          health_points, damage, dexter, regene, catchphrase)

        self.buffed_dexter = int(dexter+(dexter*0.2))

    def newstr(self):
        return super().__str__().replace(str(self.dexter), str(self.buffed_dexter))

    def blessed(): ...


class Undead_hero(Mainhero):
    fly = False
    proklytay_zemly = True

    def __init__(self, name, nikename, ras, superpower, health_points, damage, dexter, regene, catchphrase):
        Mainhero.__init__(self, name, nikename, ras, superpower,
                          health_points, damage, dexter, regene, catchphrase)

        self.buffed_regene = regene+(regene*0.1)

    def newstr(self):
        return super().__str__().replace(str(self.regene), str(self.buffed_regene))

    def kunibalizb(): ...


name = "Самуро из клана Пылающий клинок"
nikename = "Мастер Клинка"
ras = "Орк"
superpower = "Танец клинков"
health_points = 1900
catchphrase = "Мой клинок жаждет крови"
dexter = 100
damage = 200
regene = 10

name_2 = "Нер-Зул"
nikename_2 = "Король Лич"
ras_2 = "Нежить"
superpower_2 = "Порча"
health_points_2 = 1100
catchphrase_2 = "Во славу мертвых"
dexter_2 = 200
damage_2 = 175
regene_2 = 10

hero_1 = Ork_hero(name, nikename, ras, superpower,
                  health_points, damage, dexter, regene, catchphrase)
print(hero_1.newstr())

print()

hero_2 = Undead_hero(name_2, nikename_2, ras_2, superpower_2,
                     health_points_2, damage_2, dexter_2, regene_2, catchphrase_2)
print(hero_2.newstr())
