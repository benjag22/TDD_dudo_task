from src.juego.dado import Dado

class Cacho:
    def __init__(self):
        self.dados = [Dado() for _ in range(5)]
