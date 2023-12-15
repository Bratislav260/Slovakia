class Hum:
    # свойство класса
    head = True

    # конструктор класса - инициализатор
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # метод - функция внутри класса
    def printHEAD(self):
        print(self.head)

    # магические методы

    def __str__(self):
        return f'{self.head} {self.name} {self.age}'

    def __len__(self):
        return len(self.name)


# обьект или экземпляр класса

beka = Hum('beka', 20)
beka.printHEAD()

ainura = Hum('ainura', 17)

print(ainura)
print(beka)
print(len(ainura))
# print(abs(ainura))
