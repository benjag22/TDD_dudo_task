import pytest
from src.juego.cacho import Cacho


def test_cacho_contiene_5_dados():
    cacho = Cacho()
    assert len(cacho.dados) == 5

def test_cacho_lanza_todos_los_dados():
    cacho = Cacho()
    resultados = cacho.lanzar_dados()
    assert all(1 <= resultado <= 6 for resultado in resultados)

def test_validar_cantidad_dados_al_quitar():
    cacho = Cacho()
    n_dados = cacho.obtener_cantidad_de_dados()
    resultado = cacho.quitar_dado()
    assert (n_dados - 1 == resultado) and (resultado >= 0)