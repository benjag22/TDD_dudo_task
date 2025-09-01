import pytest
from src.juego.cacho import Cacho

def test_cacho_contiene_5_dados():
    """
    Verifica que al inicializar un juego de Cacho, se creen exactamente 5 dados.
    """
    cacho = Cacho()
    assert len(cacho.dados) == 5  # Debe haber 5 dados al iniciar

def test_cacho_lanza_todos_los_dados():
    """
    Verifica que al lanzar los dados de Cacho, todos los valores estén entre 1 y 6.
    """
    cacho = Cacho()
    resultados = cacho.lanzar_dados()

    # Cada dado lanzado debe tener un valor válido (1 a 6)
    assert all(1 <= resultado <= 6 for resultado in resultados)

def test_validar_cantidad_dados_al_quitar():
    """
    Verifica que al quitar un dado, la cantidad de dados restantes disminuya en 1
    y nunca sea negativa.
    """
    cacho = Cacho()
    n_dados = cacho.obtener_cantidad_de_dados()
    resultado = cacho.quitar_dado()

    # La cantidad de dados debe disminuir en 1 y permanecer >= 0
    assert (n_dados - 1 == resultado) and (resultado >= 0)
