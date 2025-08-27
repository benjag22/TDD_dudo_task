class GestorPartida:
    
    def __init__(self, jugadores):

        self.dados_por_jugador = {}
        
        for jugador in jugadores:
            self.dados_por_jugador[jugador] = 5
    
    def obtener_dados_jugador(self, nombre_jugador):

        return self.dados_por_jugador[nombre_jugador]