import pytest
from src.juego.dado import Dado

def test_dado_devuelve_numero_entre_1_y_6():
    d = Dado()
    resultado = d.lanzar()
    assert 1 <= resultado <= 6


def test_dado_define_su_valor():
    d = Dado()
    resultado = d.definir(1)
    assert resultado == "As"
    resultado = d.definir(2)
    assert resultado == "Tonto"
    resultado = d.definir(3)
    assert resultado == "Tren"
    resultado = d.definir(4)
    assert resultado == "Cuadra"
    resultado = d.definir(5)
    assert resultado == "Quina"
    resultado = d.definir(6)
    assert resultado == "Sexto"