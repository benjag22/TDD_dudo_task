class ContadorPintas:
    """
    Clase para contar la cantidad de veces que aparece una determinada pinta (número) 
    en una lista de dados o en varios lanzamientos de Cacho.
    También permite contar considerando los ases (1) como comodines.
    """

    def contar_apariciones(self, dados: list[int], pinta: int) -> int:
        """
        Cuenta cuántas veces aparece una pinta específica en una lista de dados.

        Args:
            dados (list[int]): Lista de valores de dados.
            pinta (int): Número que se desea contar (1 a 6).

        Returns:
            int: Cantidad de veces que aparece la pinta en la lista de dados.
        """
        return dados.count(pinta)

    def contar_apariciones_con_ases(self, dados: list[int], pinta: int) -> int:
        """
        Cuenta cuántas veces aparece una pinta específica en una lista de dados,
        considerando los ases (1) como comodines, excepto si solo hay un dado.

        Args:
            dados (list[int]): Lista de valores de dados.
            pinta (int): Número que se desea contar (1 a 6).

        Returns:
            int: Cantidad de apariciones de la pinta, sumando los ases como comodines.
        """
        if len(dados) == 1:
            return dados.count(pinta)
        return dados.count(pinta) + dados.count(1)

    def contar_en_todos_los_dados(
        self,
        todos_los_cachos: list[list[int]],
        pinta: int,
        usar_ases_como_comodines: bool = True
    ) -> int:
        """
        Cuenta cuántas veces aparece una pinta específica en varios lanzamientos de dados,
        pudiendo considerar los ases (1) como comodines según el parámetro.

        Args:
            todos_los_cachos (list[list[int]]): Lista de lanzamientos de dados, cada uno es una lista de enteros.
            pinta (int): Número que se desea contar (1 a 6).
            usar_ases_como_comodines (bool, optional): Si es True, los ases se cuentan como la pinta buscada. 
                                                       Por defecto es True.

        Returns:
            int: Total de apariciones de la pinta en todos los lanzamientos.
        """
        total = 0
        for cacho in todos_los_cachos:
            if usar_ases_como_comodines:
                total += self.contar_apariciones_con_ases(cacho, pinta)
            else:
                total += self.contar_apariciones(cacho, pinta)
        return total
