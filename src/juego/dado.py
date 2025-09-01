import random

class Dado:
    """
    Clase que representa un dado de seis caras.
    Permite lanzar el dado, obtener su valor numérico
    y traducirlo a un nombre específico.
    """

    valor: int  # Valor actual del dado (entre 1 y 6)

    def __init__(self):
        """
        Inicializa el dado con valor 0 (no lanzado aún).
        """
        self.valor = 0

    def lanzar(self):
        """
        Simula el lanzamiento del dado, generando un número aleatorio entre 1 y 6.
        
        Returns:
            int: El valor obtenido tras lanzar el dado.
        """
        self.valor = random.randint(1, 6)
        return self.valor

    def getValor(self):
        """
        Obtiene el valor actual del dado.
        
        Returns:
            int: El valor guardado en el dado (0 si no se ha lanzado).
        """
        return self.valor

    def definir(self, valor):
        """
        Devuelve un nombre asociado al valor del dado.
        
        Args:
            valor (int): Número entre 1 y 6 que representa el resultado del dado.
        
        Returns:
            str: Nombre correspondiente al valor.
        """
        match valor:
            case 1:
                return "As"
            case 2:
                return "Tonto"
            case 3:
                return "Tren"
            case 4:
                return "Cuadra"
            case 5:
                return "Quina"
            case 6:
                return "Sexto"

# Diccionario de equivalencias (opcional como referencia):
# 1: "As", 2: "Tonto", 3: "Tren", 4: "Cuadra", 5: "Quina", 6: "Sexto"
