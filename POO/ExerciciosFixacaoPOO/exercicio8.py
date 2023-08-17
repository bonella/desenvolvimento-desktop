"""
Exercício 8: Monitoramento de Sensores
Crie uma classe chamada "Sensor" que represente um sensor de temperatura em um sistema de monitoramento.
O sensor deve ter os seguintes atributos:
identificador (string), unidade de medida (string) e valor de temperatura atual (float).
Implemente métodos para atualizar o valor da temperatura e para exibir a leitura
atual.
"""

class Sensor:

    def __init__(self, identificador, unidade):
        self.identificador = identificador
        self.unidade = unidade
        self.temperatura_atual = 0.0

    def atualizar_temperatura(self, temperatura:float):
        self.temperatura_atual = temperatura

    def exibir_leitura(self):
        print(f'A temperatura atual é {self.temperatura_atual} graus {self.unidade}.')

sensor = Sensor('Plantas', 'Celsius')
sensor.exibir_leitura()
sensor.atualizar_temperatura(25.6)
sensor.exibir_leitura()
