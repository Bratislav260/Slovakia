class Bank:

    def __init__(self, _name, _balanse):
        self.name = _name
        self.balanse = _balanse

    def moneyX(self, plus):
        self.balanse += plus

    def __str__(self):
        return "{},\n{}".format(self.name, self.balanse)

    def _kill(self):
        self.balanse *= 0

    def __jackpot(self):
        self.balanse *= 10

    def _skinut(self, shet_1, shet_2):
        self.balanse = shet_1 + shet_2
        print("Деньги успешно переведены!")


beka = Bank("Goblin", 1000)
teka = Bank("Speer", 1300)

print(beka)
print(teka)
print()
beka._skinut(beka.balanse, teka.balanse)
print()
print(beka)
