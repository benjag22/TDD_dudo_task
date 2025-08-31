class ContadorPintas:

    def contar_apariciones(self, dados: list[int], pinta: int) -> int:
        return dados.count(pinta)

    def contar_apariciones_con_ases(self, dados: list[int], pinta: int) -> int:
        if len(dados) == 1:
            return dados.count(pinta)

        return dados.count(pinta) + dados.count(1)