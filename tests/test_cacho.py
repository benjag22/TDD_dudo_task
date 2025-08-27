import pytest
from src.juego.cacho import Cacho


def test_cacho_contiene_5_dados():
    cacho = Cacho()
    assert len(cacho.dados) == 5

def test_cacho_lanza_todos_los_dados():
    cacho = Cacho()
    resultados = cacho.lanzar_dados()
    assert all(1 <= resultado <= 6 for resultado in resultados)