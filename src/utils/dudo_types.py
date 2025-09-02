from dataclasses import dataclass
from enum import Enum

class TipoResultado(Enum):
    """
    Enumeración que define quién pierde en una acción de dudo.
    """
    DUDADOR = "dudador"
    APOSTADOR = "apostador"


@dataclass
class Apuesta:
    """
    Representa una apuesta realizada por un jugador en el juego.
    
    Attributes:
        cantidad (int): Cantidad de dados apostados.
        pinta (int): Valor de la cara del dado apostada (1-6).
        jugador (str): Nombre del jugador que realiza la apuesta.
    """
    cantidad: int
    pinta: int
    jugador: str


@dataclass
class ResultadoDudo:
    """
    Resultado de procesar una acción de dudo contra una apuesta.
    
    Attributes:
        apuesta_es_cierta (bool): Si la apuesta era correcta o no.
        quien_pierde (TipoResultado): Quién pierde la ronda (dudador o apostador).
        dados_reales (int): Cantidad real de dados con la pinta apostada.
        dados_apostados (int): Cantidad de dados que se apostó originalmente.
    """
    apuesta_es_cierta: bool
    quien_pierde: TipoResultado
    dados_reales: int
    dados_apostados: int


@dataclass
class ResultadoCalzar:
    """
    Resultado de procesar una acción de calzar contra una apuesta.
    
    Attributes:
        calce_exitoso (bool): Si el calzar fue exitoso (cantidad exacta).
        quien_gana_dado (str | None): Quién gana un dado extra, None si falló.
        dados_reales (int): Cantidad real de dados con la pinta apostada.
        dados_apostados (int): Cantidad de dados que se apostó originalmente.
    """
    calce_exitoso: bool
    quien_gana_dado: str | None
    dados_reales: int
    dados_apostados: int