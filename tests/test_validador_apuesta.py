import pytest

def test_primera_apuesta_permitida_sin_ases():
    validador = ValidadorApuesta()
    nueva_cantidad = 2
    nueva_pinta = 1
    dados_restantes = 5
    assert validador.validar_apuesta(nueva_cantidad, nueva_pinta, dados_restantes) is False

