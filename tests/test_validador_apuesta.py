import pytest
from src.juego.validador_apuesta import ValidadorApuesta

def test_primera_apuesta_permitida_sin_ases():
    validador = ValidadorApuesta()
    nueva_cantidad = 2
    nueva_pinta = 1
    dados_restantes = 5
    assert validador.validar_apuesta(nueva_cantidad, nueva_pinta, dados_restantes) is False

def test_conversion_a_ases_cantidad_par():
    validador = ValidadorApuesta()
    nueva_cantidad = 6
    nueva_pinta = 4
    dados_restantes = 5
    assert validador.validar_apuesta(nueva_cantidad, nueva_pinta, dados_restantes) == True
    nueva_cantidad = (nueva_cantidad // 2) + 1
    nueva_pinta = 1
    dados_restantes = 5
    assert validador.validar_apuesta(nueva_cantidad, nueva_pinta, dados_restantes) == True
