class Animal:
    def fala(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return 'Au Au'

class Gatineo(Animal):
    def falar(self):
        return 'Miau'

def animal_falando(animal):
    print(animal.falar())

cao = Cachorro()
gato = Gatineo()

animal_falando(cao)
animal_falando(gato)
