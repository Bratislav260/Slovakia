class Hum:  # суперкласс,родительский класс
    head = 1

    def __init__(self, name, age):
        self.name = name
        self.возраст = age

    def run(self):
        print(self.name, 'бегает от своего возраста', self.возраст)

    def __str__(self):
        return f'{self.name} {self.возраст}'


class Hum2(Hum):  # дочерний класс

    def __init__(self, name, age, height):
        super().__init__(name, age)
        # Hum.__init__(self,name,age)
        self.height = height

    def agetrue(self):
        print(2023 - self.возраст)

    def run(self):
        print(self.name, ' смирился со своим возрастом')

    def newstr(self):
        return " ".join([super().__str__(), str(self.height)])


# azamat = Hum2('азамат', 16, 180)
# azamat.agetrue()

roman = Hum2('Роман', 20, 176)
print(roman.newstr())
