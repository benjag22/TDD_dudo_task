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