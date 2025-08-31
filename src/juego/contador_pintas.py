class ContadorPintas:

    def contar_apariciones(self, dados: list[int], pinta: int) -> int:
        return dados.count(pinta)

    def contar_apariciones_con_ases(self, dados: list[int], pinta: int) -> int:

        if len(dados) == 1:
            return dados.count(pinta)

        return dados.count(pinta) + dados.count(1)

    def contar_en_todos_los_dados(self, todos_los_cachos: list[list[int]], pinta: int,
                                  usar_ases_como_comodines: bool = True) -> int:
        total = 0
        for cacho in todos_los_cachos:
            if usar_ases_como_comodines:
                total += self.contar_apariciones_con_ases(cacho, pinta)
            else:
                total += self.contar_apariciones(cacho, pinta)
        return total
