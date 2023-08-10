class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def emitir_som(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        self.__raca = raca

    def obter_raca(self):
        return self.__raca

    def emitir_som(self):
        return 'O cachorro late.'

class Gato(Animal):
    def __init__(self, nome, especie, pelagem):
        super().__init__(nome, especie)
        self.__pelagem = pelagem

    def obter_pelagem(self):
        return self.__pelagem

cachorro = Cachorro('Bob', 'Canino', 'PitBull')
print(f'Meu cachorro {cachorro.nome} é da espécie {cachorro.especie} e raça {cachorro.obter_raca()}')
print(cachorro.emitir_som())

gato = Gato('Mimi', 'Felino', 'Fofinho')
print(f'Meu gato {gato.nome} é da espécie {gato.especie} e raça {gato.obter_pelagem()}')
print(gato.emitir_som())
