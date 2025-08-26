import pytest

def test_dado_devuelve_numero_entre_1_y_6():
    from dado import Dado   # aún no existe dado.py
    d = Dado()
    resultado = d.lanzar()
    assert 1 <= resultado <= 6
