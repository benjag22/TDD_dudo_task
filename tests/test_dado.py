import pytest
from src.juego.dado import Dado

def test_dado_devuelve_numero_entre_1_y_6():
    d = Dado()
    resultado = d.lanzar()
    assert 1 <= resultado <= 6


