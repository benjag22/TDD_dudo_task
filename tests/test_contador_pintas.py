import pytest
from src.juego.contador_pintas import ContadorPintas

def test_contar_apariciones():
    contador = ContadorPintas()
    assert contador.contar_apariciones([1, 4, 6, 1, 3], 4) == 1

def test_contar_apaciones_con_comodines():
    contador = ContadorPintas()
    assert contador.contar_apariciones_con_ases([1, 4, 6, 1, 3], 4) == 3

def test_contar_apaciones_con_comodines_con_un_dado():
    contador = ContadorPintas()
    assert contador.contar_apariciones_con_ases([1], 1) == 1

def test_contar_todos_los_cachos():
    contador = ContadorPintas()
    usar_ases_como_comidines = True

    cachos = [
        [1, 2, 2, 4, 5], # pinta 1: 2 si ases = true y 1 si ases = false
        [3, 2],
        [1] # pinta 1: 1 siempre
    ]

    assert contador.contar_en_todos_los_dados(cachos, 1, usar_ases_como_comidines) == 3

    usar_ases_como_comidines = False

    assert contador.contar_en_todos_los_dados(cachos, 1, usar_ases_como_comidines) == 2