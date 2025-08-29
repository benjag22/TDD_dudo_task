class ValidadorApuesta:

    cantidad_actual:int
    pinta_actual:int

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
