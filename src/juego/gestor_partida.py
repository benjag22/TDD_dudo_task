import random
from dataclasses import dataclass
from typing import Optional

from src.juego.arbitro_ronda import ArbitroRonda
from src.juego.cacho import Cacho
from src.juego.validador_apuesta import ValidadorApuesta
from src.utils.dudo_types import Apuesta, TipoResultado


@dataclass
class EstadoJugador:
    dados: int
    cacho: Cacho

    @property
    def tiene_un_solo_dado(self) -> bool:
        return self.dados == 1

    @property
    def esta_eliminado(self) -> bool:
        return self.dados == 0


@dataclass
class Jugador:
    nombre: str
    estado: EstadoJugador


@dataclass
class ConfiguracionRondaEspecial:
    activa: bool = False
    tipo: str = ""
    pinta_fija: Optional[int] = None
    iniciador: Optional[str] = None


class GestorPartida:
    _jugadores: list[Jugador]
    _jugadores_activos: list[Jugador]
    _validador: ValidadorApuesta
    _arbitro: ArbitroRonda
    _apuesta_actual: Optional[Apuesta]
    _direccion_clockwise: bool
    _iniciador_ronda: str | None
    _indice_turno_actual: int
    _ronda_especial: bool

    def __init__(self, jugadores: list[str]):

        self._jugadores = [Jugador(nombre, EstadoJugador(5, Cacho())) for nombre in jugadores]
        self._jugadores_activos = self._jugadores.copy()
        self._validador = ValidadorApuesta()
        self._arbitro = ArbitroRonda()

        self._apuesta_actual: Optional[Apuesta] = None
        self._direccion_clockwise = True
        self._iniciador_ronda = None
        self._indice_turno_actual = 0

        self._ronda_especial = False

    def iniciar_partida(self) -> dict:

        tiradas = self._determinar_iniciador()
        return {
            "tiradas": tiradas,
            "iniciador": self._iniciador_ronda
        }

    def obtener_dados_jugador(self, nombre_jugador):
        jugador = self._buscar_jugador(nombre_jugador)
        return jugador.estado.dados if jugador else 0

    def quitar_dado_jugador(self, nombre_jugador: str) -> bool:
        jugador = self._buscar_jugador(nombre_jugador)
        if not jugador or jugador.estado.dados <= 0:
            return False

        jugador.estado.dados -= 1
        jugador.estado.cacho.quitar_dado()

        if jugador.estado.esta_eliminado:
            self._jugadores_activos.remove(jugador)
            self._ajustar_turno_tras_eliminacion(nombre_jugador)
            return True

        return False

    def establecer_perdedor_ronda(self, nombre_jugador: str) -> None:
        self._iniciador_ronda = nombre_jugador
        self._establecer_turno_en_jugador(nombre_jugador)

    def obtener_iniciador_ronda(self) -> str:
        return self._iniciador_ronda

    def tiene_jugador_un_solo_dado(self, nombre_jugador: str) -> bool:
        jugador = self._buscar_jugador(nombre_jugador)
        return jugador.estado.tiene_un_solo_dado if jugador else False

    def obtener_jugador_actual(self) -> str:
        return self._jugadores_activos[self._indice_turno_actual].nombre

    def establecer_direccion(self, clockwise: bool) -> None:
        self._direccion_clockwise = clockwise

    def avanzar_turno(self) -> str:
        if self._direccion_clockwise:
            self._indice_turno_actual = (self._indice_turno_actual + 1) % len(self._jugadores_activos)
        else:
            self._indice_turno_actual = (self._indice_turno_actual - 1) % len(self._jugadores_activos)

        return self.obtener_jugador_actual()

    def procesar_dudo(self, dudador: str) -> dict:
        if not self._apuesta_actual:
            return {"error": "No hay apuesta para dudar"}

        todos_los_cachos = self._obtener_todos_los_dados_como_listas()
        usar_ases_como_comodines = not self._ronda_especial

        resultado = self._arbitro.determinar_resultado_dudo(
            self._apuesta_actual,
            todos_los_cachos,
            usar_ases_como_comodines
        )

        perdedor = dudador if resultado.quien_pierde == TipoResultado.DUDADOR else self._apuesta_actual.jugador
        self.quitar_dado_jugador(perdedor)
        self.establecer_perdedor_ronda(perdedor)
        self.preparar_nueva_ronda()

        return {
            "apuesta_es_cierta": resultado.apuesta_es_cierta,
            "quien_pierde": resultado.quien_pierde.value,
            "dados_reales": resultado.dados_reales,
            "dados_apostados": resultado.dados_apostados,
            "perdedor": perdedor,
            "dados_mostrados": self._obtener_dados_todos_jugadores()
        }

    def realizar_apuesta(self, jugador: str, cantidad: int, pinta: int) -> dict:
        jugador_obj = self._buscar_jugador(jugador)
        if not jugador_obj:
            return {"valida": False, "mensaje": "Jugador no encontrado"}

        dados_jugador = jugador_obj.estado.dados

        if not self._validador.validar_apuesta(cantidad, pinta, dados_jugador):
            return {"valida": False, "mensaje": "Apuesta inválida"}

        self._apuesta_actual = Apuesta(cantidad, pinta, jugador)

        return {
            "valida": True,
            "apuesta": Apuesta(jugador=jugador, cantidad=cantidad, pinta=pinta),
        }

    def preparar_nueva_ronda(self) -> None:
        self._validador.reiniciar()
        self._apuesta_actual = None
        self._ronda_especial = False

        self._lanzar_todos_los_dados()

    def nueva_ronda(self) -> None:
        self.preparar_nueva_ronda()
        if self._iniciador_ronda:
            self._establecer_turno_en_jugador(self._iniciador_ronda)

    def es_fin_del_juego(self) -> bool:
        return len(self._jugadores_activos) <= 1

    def obtener_ganador(self) -> str | None:
        if len(self._jugadores_activos) == 1:
            return self._jugadores_activos[0].nombre
        return None

    def obtener_jugadores_activos(self) -> list[str]:
        return [jugador.nombre for jugador in self._jugadores_activos]

    def _determinar_iniciador(self) -> dict[str, int]:
        nombres_jugadores = [jugador.nombre for jugador in self._jugadores_activos]
        participantes = nombres_jugadores.copy()
        tiradas = {}

        while len(participantes) > 1:
            for jugador in participantes:
                tiradas[jugador] = random.randint(1, 6)

            max_tirada = max(tiradas.values())
            participantes = [jugador for jugador, tirada in tiradas.items() if tirada == max_tirada]

        self._iniciador_ronda = participantes[0]
        self._establecer_turno_en_jugador(self._iniciador_ronda)

        return tiradas

    def _lanzar_todos_los_dados(self) -> None:
        for jugador in self._jugadores_activos:
            if jugador.estado.dados > 0:
                jugador.estado.cacho.lanzar_dados()

    def _buscar_jugador(self, nombre: str) -> Jugador | None:
        for jugador in self._jugadores:
            if jugador.nombre == nombre:
                return jugador
        return None

    def _establecer_turno_en_jugador(self, nombre: str) -> None:
        for i, jugador in enumerate(self._jugadores_activos):
            if jugador.nombre == nombre:
                self._indice_turno_actual = i
                break

    def _ajustar_turno_tras_eliminacion(self, jugador_eliminado: str) -> None:
        indice_eliminado = -1
        for i, jugador in enumerate(self._jugadores_activos):
            if jugador.nombre == jugador_eliminado:
                indice_eliminado = i
                break

        if indice_eliminado != -1:
            if indice_eliminado < self._indice_turno_actual:
                self._indice_turno_actual -= 1
            elif indice_eliminado == self._indice_turno_actual and self._indice_turno_actual >= len(
                    self._jugadores_activos):
                self._indice_turno_actual = 0

    def _obtener_todos_los_dados_como_listas(self) -> list[list[int]]:
        return [jugador.estado.cacho.obtener_valores() for jugador in self._jugadores_activos]

    def _obtener_dados_todos_jugadores(self) -> dict[str, list[int]]:
        return {
            jugador.nombre: jugador.estado.cacho.obtener_valores()
            for jugador in self._jugadores_activos
        }
