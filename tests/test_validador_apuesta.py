import pytest
from src.juego.validador_apuesta import ValidadorApuesta

def test_primera_apuesta_permitida_sin_ases():
    """
    Verifica que la primera apuesta no pueda ser un as (1) si hay más de un dado disponible.
    """
    validador = ValidadorApuesta()
    nueva_cantidad = 2
    nueva_pinta = 1
    dados_restantes = 5

    # La apuesta inicial con un as no está permitida cuando hay más de un dado
    assert validador.validar_apuesta(nueva_cantidad, nueva_pinta, dados_restantes) is False

def test_conversion_a_ases_cantidad_par():
    """
    Verifica la conversión correcta de apuestas normales a ases cuando la cantidad es par.
    Comprueba que la nueva apuesta con ases cumple con la cantidad mínima requerida.
    """
    validador = ValidadorApuesta()
    nueva_cantidad = 6
    nueva_pinta = 4
    dados_restantes = 5

    # Primera apuesta normal
    assert validador.validar_apuesta(nueva_cantidad, nueva_pinta, dados_restantes) == True

    # Ahora se apuesta con ases (1)
    nueva_cantidad = (nueva_cantidad // 2) + 1
    nueva_pinta = 1
    dados_restantes = 5

    # La apuesta con ases debe ser válida si cumple la cantidad mínima
    assert validador.validar_apuesta(nueva_cantidad, nueva_pinta, dados_restantes) == True

def test_conversion_desde_ases_con_cantidad_minima():
    """
    Verifica la conversión desde ases a otra pinta. 
    Asegura que se cumpla la cantidad mínima para superar la apuesta anterior.
    """
    validador = ValidadorApuesta()

    # Primera apuesta normal
    nueva_cantidad = 7
    nueva_pinta = 4
    dados_restantes = 5
    assert validador.validar_apuesta(nueva_cantidad, nueva_pinta, dados_restantes) == True

    # Configuramos la apuesta actual como ases
    validador.cantidad_actual = 2
    validador.pinta_actual = 1

    # Cantidad mínima correcta al pasar de ases a otra pinta
    assert validador.validar_apuesta(5, 6, 12) == True
    assert validador.validar_apuesta(6, 3, 12) == True

    # Cantidades insuficientes para superar la apuesta con ases
    validador.cantidad_actual = 4
    validador.pinta_actual = 1
    assert validador.validar_apuesta(8, 5, 12) == False  # mínimo requerido: 9
    assert validador.validar_apuesta(7, 6, 12) == False  # mínimo requerido: 9
