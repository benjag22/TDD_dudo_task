import math


class ValidadorApuesta:
    cantidad_actual: int
    pinta_actual: int

    def __init__(self):
        self.cantidad_actual = 0
        self.pinta_actual = 0

    def validar_apuesta(self, nueva_cantidad: int, nueva_pinta: int, dados_restantes: int) -> bool:

        if self.cantidad_actual == 0:
            if nueva_pinta == 1 and dados_restantes > 1:
                return False

            self.cantidad_actual = nueva_cantidad
            self.pinta_actual = nueva_pinta
            return True

        es_valida = False

        if nueva_pinta == 1 and self.pinta_actual != 1:
            cantidad_minima = self._convertir_a_ases(self.cantidad_actual)
            es_valida = nueva_cantidad >= cantidad_minima

        if es_valida:
            self.cantidad_actual = nueva_cantidad
            self.pinta_actual = nueva_pinta

        return es_valida

    def _convertir_a_ases(self, cantidad: int) -> int:
        return (cantidad // 2) + 1 if cantidad % 2 == 0 else math.ceil(cantidad / 2)
