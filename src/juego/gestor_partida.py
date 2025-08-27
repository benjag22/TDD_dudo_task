class GestorPartida:
    
    def __init__(self, jugadores):

        self.dados_por_jugador = {}
        
        for jugador in jugadores:
            self.dados_por_jugador[jugador] = 5
            
        self.iniciador_ronda = None
    
    def obtener_dados_jugador(self, nombre_jugador):

        return self.dados_por_jugador[nombre_jugador]
    
    def quitar_dado_jugador(self, nombre_jugador):

        if self.dados_por_jugador[nombre_jugador] > 0:
            self.dados_por_jugador[nombre_jugador] -= 1
    
    def establecer_perdedor_ronda(self, nombre_jugador): 
        self.iniciador_ronda = nombre_jugador
    
    def obtener_iniciador_ronda(self):
        return self.iniciador_ronda
    
    def tiene_jugador_un_solo_dado(self, nombre_jugador):
        return self.dados_por_jugador[nombre_jugador] == 1