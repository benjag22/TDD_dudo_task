from src.juego.dado import Dado

class Cacho:
    """
    Clase que representa un juego de Cacho (dados).
    Contiene cinco dados y permite lanzarlos, obtener sus valores,
    contar cuántos dados hay y quitar un dado del juego.
    """

    def __init__(self) -> None:
        """
        Inicializa el juego creando una lista de 5 objetos Dado.
        """
        self.dados = [Dado() for _ in range(5)]

    def lanzar_dados(self) -> list[int]:
        """
        Lanza todos los dados del juego.
        
        Returns:
            list[int]: Lista de los valores obtenidos tras lanzar cada dado.
        """
        return [dado.lanzar() for dado in self.dados]

    def obtener_cantidad_de_dados(self) -> int:
        """
        Obtiene la cantidad actual de dados disponibles en el juego.
        
        Returns:
            int: Número de dados restantes.
        """
        return len(self.dados)

    def obtener_valores(self) -> list[int]:
        """
        Obtiene los valores actuales de todos los dados sin lanzarlos nuevamente.
        
        Returns:
            list[int]: Lista de valores de cada dado.
        """
        return [dado.getValor() for dado in self.dados]

    def quitar_dado(self) -> int:
        """
        Quita un dado del juego (el último de la lista) y devuelve
        la cantidad de dados restantes.
        
        Returns:
            int: Cantidad de dados que quedan después de quitar uno.
        """
        self.dados.pop()
        return self.obtener_cantidad_de_dados()
