import pytest
from src.juego.dado import Dado

def test_dado_devuelve_numero_entre_1_y_6():
    """
    Verifica que al lanzar un dado, el valor devuelto esté siempre entre 1 y 6.
    """
    d = Dado()
    resultado = d.lanzar()

    # El valor del dado debe estar en el rango válido
    assert 1 <= resultado <= 6

def test_dado_define_su_valor():
    """
    Verifica que el método definir devuelva el nombre correcto
    según el valor del dado:
        1 -> "As"
        2 -> "Tonto"
        3 -> "Tren"
        4 -> "Cuadra"
        5 -> "Quina"
        6 -> "Sexto"
    """
    d = Dado()

    # Se comprueba que cada valor tenga su nombre correcto
    assert d.definir(1) == "As"
    assert d.definir(2) == "Tonto"
    assert d.definir(3) == "Tren"
    assert d.definir(4) == "Cuadra"
    assert d.definir(5) == "Quina"
    assert d.definir(6) == "Sexto"
