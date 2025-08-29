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

def test_conversion_desde_ases_con_cantidad_minima():
    validador = ValidadorApuesta()

    nueva_cantidad = 7
    nueva_pinta = 4
    dados_restantes = 5

    assert validador.validar_apuesta(nueva_cantidad, nueva_pinta, dados_restantes) == True

    validador.cantidad_actual = 2
    validador.pinta_actual = 1

    assert validador.validar_apuesta(5, 6, 12) == True  # cantidad min bien

    validador.cantidad_actual = 2
    validador.pinta_actual = 1
    assert validador.validar_apuesta(6, 3, 12) == True

    validador.cantidad_actual = 4
    validador.pinta_actual = 1

    assert validador.validar_apuesta(8, 5, 12) == False  # falta cantidad: min 9
    assert validador.validar_apuesta(7, 6, 12) == False  # falta cantidad: min 9

