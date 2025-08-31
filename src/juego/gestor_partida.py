from typing import Optional

from src.juego.arbitro_ronda import ArbitroRonda
from src.juego.cacho import Cacho
from src.juego.validador_apuesta import ValidadorApuesta
from src.utils.dudo_types import Apuesta, TipoResultado


class GestorPartida:
    def __init__(self, jugadores: list[str]):
        self.jugadores_activos = jugadores.copy()
        self.dados_por_jugador = {jugador: 5 for jugador in jugadores}

        self.cachos = {jugador: Cacho() for jugador in jugadores}
        self.validador = ValidadorApuesta()
        self.arbitro = ArbitroRonda()

        self.ronda_especial_activa = False
        self.apuesta_actual: Optional[Apuesta] = None
        self.direccion_clockwise = True
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

    def establecer_direccion(self, clockwise: bool) -> None:
        self.direccion_clockwise = clockwise

    def avanzar_turno(self) -> None:
        if self.direccion_clockwise:
            self.indice_turno_actual = (self.indice_turno_actual + 1) % len(self.jugadores_activos)
        else:
            self.indice_turno_actual = (self.indice_turno_actual - 1) % len(self.jugadores_activos)

    def procesar_dudo(self, dudador: str) -> dict:
        if not self.apuesta_actual:
            return {"error": "No hay apuesta para dudar"}

        todos_los_cachos = self._obtener_todos_los_dados_como_listas()
        usar_ases_como_comodines = not self.ronda_especial_activa

        resultado = self.arbitro.determinar_resultado_dudo(
            self.apuesta_actual,
            todos_los_cachos,
            usar_ases_como_comodines
        )

        perdedor = dudador if resultado.quien_pierde == TipoResultado.DUDADOR else self.apuesta_actual.jugador
        self.quitar_dado_jugador(perdedor)

        self.iniciador_ronda = perdedor
        self.preparar_nueva_ronda()

        return {
            "apuesta_es_cierta": resultado.apuesta_es_cierta,
            "quien_pierde": resultado.quien_pierde.value,
            "dados_reales": resultado.dados_reales,
            "dados_apostados": resultado.dados_apostados,
            "perdedor": perdedor,
        }

    def realizar_apuesta(self, jugador: str, cantidad: int, pinta: int) -> dict[str, int]:
        dados_jugador = self.dados_por_jugador[jugador]

        if not self.validador.validar_apuesta(cantidad, pinta, dados_jugador):
            return {"valida": False, "mensaje": "Apuesta inválida"}

        self.apuesta_actual = Apuesta( cantidad, pinta, jugador)

        return {
            "valida": True,
            "apuesta": {
                "jugador": jugador,
                "cantidad": self.apuesta_actual.cantidad,
                "pinta": self.apuesta_actual.pinta
            }
        }

    def preparar_nueva_ronda(self) -> None:
        self.validador.reiniciar()
        self.apuesta_actual = None
        self.ronda_especial_activa = False

        if self.iniciador_ronda in self.jugadores_activos:
            self.indice_turno_actual = self.jugadores_activos.index(self.iniciador_ronda)

    def es_fin_del_juego(self) -> bool:
        return len(self.jugadores_activos) <= 1

    def obtener_ganador(self) -> str | None:
        if len(self.jugadores_activos) == 1:
            return self.jugadores_activos[0]
        return None

    def _obtener_todos_los_dados_como_listas(self) -> list[list[int]]:
        return [cacho.obtener_valores() for cacho in self.cachos.values()]
