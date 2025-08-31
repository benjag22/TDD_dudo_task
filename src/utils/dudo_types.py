from dataclasses import dataclass
from enum import Enum

class TipoResultado(Enum):
    DUDADOR = "dudador"
    APOSTADOR = "apostador"


@dataclass
class Apuesta:
    cantidad: int
    pinta: int
    jugador: str


@dataclass
class ResultadoDudo:
    apuesta_es_cierta: bool
    quien_pierde: TipoResultado
    dados_reales: int
    dados_apostados: int


@dataclass
class ResultadoCalzar:
    calce_exitoso: bool
    quien_gana_dado: str | None
    dados_reales: int
    dados_apostados: int