import math

class ValidadorApuesta:
    """
    Clase que valida las apuestas en un juego de dados tipo Cacho o Liar's Dice.
    Mantiene la apuesta actual (cantidad y pinta) y permite validar nuevas apuestas
    según las reglas del juego.
    """

    cantidad_actual: int
    pinta_actual: int

    def __init__(self):
        """
        Inicializa el validador con apuesta actual en cero.
        """
        self.cantidad_actual = 0
        self.pinta_actual = 0

    def validar_apuesta(self, nueva_cantidad: int, nueva_pinta: int, dados_restantes: int) -> bool:
        """
        Valida si una nueva apuesta es válida según las reglas:
        - La nueva apuesta debe ser mayor que la anterior o igual en cantidad
          pero con una pinta mayor.
        - Se aplican reglas especiales cuando la apuesta involucra ases (1).

        Args:
            nueva_cantidad (int): Cantidad de dados apostados en la nueva apuesta.
            nueva_pinta (int): Pinta de los dados apostados (1 a 6).
            dados_restantes (int): Número de dados que tiene el jugador activo.

        Returns:
            bool: True si la apuesta es válida, False en caso contrario.
        """
        # Primera apuesta
        if self.cantidad_actual == 0:
            if nueva_pinta == 1 and dados_restantes > 1:
                return False  # No se permite empezar con ases si hay más de un dado
            self.cantidad_actual = nueva_cantidad
            self.pinta_actual = nueva_pinta
            return True

        es_valida = False

        # Regla para apuestas con ases
        if nueva_pinta == 1 and self.pinta_actual != 1:
            cantidad_minima = self._convertir_a_ases(self.cantidad_actual)
            es_valida = nueva_cantidad >= cantidad_minima

        # Regla para pasar de ases a otra pinta
        elif self.pinta_actual == 1 and nueva_pinta != 1:
            cantidad_minima = self._convertir_desde_ases(self.cantidad_actual)
            es_valida = nueva_cantidad >= cantidad_minima

        # Apuesta normal
        else:
            if nueva_cantidad > self.cantidad_actual:
                es_valida = True
            elif nueva_cantidad == self.cantidad_actual and nueva_pinta > self.pinta_actual:
                es_valida = True

        # Actualiza la apuesta actual si es válida
        if es_valida:
            self.cantidad_actual = nueva_cantidad
            self.pinta_actual = nueva_pinta

        return es_valida

    def reiniciar(self):
        """
        Reinicia la apuesta actual a cero.
        """
        self.cantidad_actual = 0
        self.pinta_actual = 0

    def _convertir_a_ases(self, cantidad: int) -> int:
        """
        Convierte una cantidad normal a la cantidad equivalente en ases (1).

        Args:
            cantidad (int): Cantidad actual de dados.

        Returns:
            int: Cantidad mínima de ases necesaria para superar la apuesta.
        """
        return (cantidad // 2) + 1 if cantidad % 2 == 0 else math.ceil(cantidad / 2)

    def _convertir_desde_ases(self, cantidad: int) -> int:
        """
        Convierte una cantidad de ases a la cantidad equivalente en otra pinta.

        Args:
            cantidad (int): Cantidad de ases apostados.

        Returns:
            int: Cantidad mínima necesaria en otra pinta para superar la apuesta.
        """
        return (cantidad * 2) + 1
