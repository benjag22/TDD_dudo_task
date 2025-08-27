from src.juego.dado import Dado

class Cacho:

    def __init__(self) -> None:
        self.dados = [Dado() for _ in range(5)]

    def lanzar_dados(self) -> list[int]:
        return [dado.lanzar() for dado in self.dados]

    def obtener_cantidad_de_dados(self) -> int:
        return len(self.dados)

    def quitar_dado(self) -> int:
        self.dados.pop()
        return self.obtener_cantidad_de_dados()