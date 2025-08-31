class GestorPartida:
    def __init__(self, jugadores: list[str]):
        self.jugadores_activos = jugadores.copy()
        self.dados_por_jugador = {jugador: 5 for jugador in jugadores}

        self.iniciador_ronda = None
        self.indice_turno_actual = 0

    def obtener_dados_jugador(self, nombre_jugador):
        return self.dados_por_jugador.get(nombre_jugador, 0)

    def quitar_dado_jugador(self, nombre_jugador):
        if self.dados_por_jugador[nombre_jugador] > 0:
            self.dados_por_jugador[nombre_jugador] -= 1
            if self.dados_por_jugador[nombre_jugador] == 0:
                self.jugadores_activos.remove(nombre_jugador)

    def establecer_perdedor_ronda(self, nombre_jugador):
        self.iniciador_ronda = nombre_jugador

    def obtener_iniciador_ronda(self):
        return self.iniciador_ronda

    def tiene_jugador_un_solo_dado(self, nombre_jugador):
        return self.dados_por_jugador[nombre_jugador] == 1

    def obtener_jugador_actual(self):
        return self.jugadores_activos[self.indice_turno_actual]

    def avanzar_turno(self):
        if len(self.jugadores_activos) > 0:
            self.indice_turno_actual = (self.indice_turno_actual + 1) % len(self.jugadores_activos)

    def es_fin_del_juego(self) -> bool:
        return len(self.jugadores_activos) <= 1

    def obtener_ganador(self) -> str | None:
        if len(self.jugadores_activos) == 1:
            return self.jugadores_activos[0]
        return None
