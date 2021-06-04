class Animals:
    def __init__(self, name, age, health,happiness):
        self.name=name
        self.age=age
        self.health=health
        self.happiness=happiness
    def display_info(self):
        print(f'Nombre: {self.name} Edad: {self.age} Salud: {self.health} Felicidad: {self.happiness}')
    def feed(self, kgs):
        self.health = self.health + 10*kgs
        self.happiness = self.happiness + 10*kgs

class Leon(Animals):
    def __init__(self, name, age, health, happiness,perso):
        super().__init__(name,age,health,happiness)
        self.perso=perso
    def display_info_leon(self):
        print(f'Personalidad {self.perso}')

class Delfin(Animals):
    def __init__(self, name, age, health, happiness,perso):
        super().__init__(name,age,health,happiness)
        self.perso=perso
    def display_info_delfin(self):
        print(f'Personalidad {self.perso}')

class Bird(Animals):
    def __init__(self, name, age, health, happiness,perso):
        super().__init__(name,age,health,happiness)
        self.perso=perso
    def display_info_bird(self):
        print(f'Personalidad {self.perso}')
        

leon01 = Leon("Leoncio", 50, 40, 10, 'El loco brígido')
leon01.display_info()
leon01.display_info_leon()
leon01.feed(2)
leon01.display_info()
leon01.display_info_leon()

delfin1 = Delfin("Dolphin segundo", 10, 20, 60, 'El loco simpático')
delfin1.display_info()
delfin1.display_info_delfin()
delfin1.feed(2)
delfin1.display_info()
delfin1.display_info_delfin()

pajaro1 = Bird("Pajaro loco", 1, 10, 20, 'El loco pitiao')
pajaro1.display_info()
pajaro1.display_info_bird()
pajaro1.feed(2)
pajaro1.display_info()
pajaro1.display_info_bird()