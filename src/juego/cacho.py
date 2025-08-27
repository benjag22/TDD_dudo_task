from src.juego.dado import Dado

class Cacho:
    def __init__(self):
        self.dados = [Dado() for _ in range(5)]
    def lanzar_dados(self):
        return [dado.lanzar() for dado in self.dados]