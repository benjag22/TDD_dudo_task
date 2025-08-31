import random

class Dado:
    valor:int
    def __init__(self):
        self.valor = 0

    def lanzar(self):
        self.valor = random.randint(1, 6)
        return self.valor

    def getValor(self):
        return self.valor

    def definir(self, valor):
        match valor:
            case 1:
                return "As"
            case 2:
                return "Tonto"
            case 3:
                return "Tren"
            case 4:
                return "Cuadra"
            case 5:
                return "Quina"
            case 6:
                return "Sexto"

#1: "As", 2: "Tonto", 3: "Tren", 4: "Cuadra", 5: "Quina", 6: "Sexto"