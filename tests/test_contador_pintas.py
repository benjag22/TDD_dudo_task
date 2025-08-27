import pytest
from src.juego.contador_pintas import ContadorPintas
def test_contar_apariciones():
    contador = ContadorPintas()
    assert contador.contar_apariciones([1, 4, 6, 1, 3], 4) == 1