import pytest
from src.juego.contador_pintas import ContadorPintas

def test_contar_apariciones():
    """
    Verifica que contar_apariciones devuelva la cantidad correcta
    de veces que aparece una pinta específica en una lista de dados.
    """
    contador = ContadorPintas()
    assert contador.contar_apariciones([1, 4, 6, 1, 3], 4) == 1  # Solo un 4 en la lista

def test_contar_apaciones_con_comodines():
    """
    Verifica que contar_apariciones_con_ases cuente los ases (1) como comodines
    además de la pinta específica.
    """
    contador = ContadorPintas()
    # Hay dos ases (1) + un 4 → total 3 contando ases como comodines
    assert contador.contar_apariciones_con_ases([1, 4, 6, 1, 3], 4) == 3

def test_contar_apaciones_con_comodines_con_un_dado():
    """
    Verifica que contar_apariciones_con_ases no trate los ases como comodines
    cuando solo hay un dado.
    """
    contador = ContadorPintas()
    assert contador.contar_apariciones_con_ases([1], 1) == 1  # Solo un dado, debe contar 1

def test_contar_todos_los_cachos():
    """
    Verifica que contar_en_todos_los_dados funcione correctamente
    contando las apariciones de una pinta en varios lanzamientos de dados,
    considerando o no los ases como comodines.
    """
    contador = ContadorPintas()
    usar_ases_como_comidines = True

    cachos = [
        [1, 2, 2, 4, 5],  # Pinta 1: 2 si ases=True, 1 si ases=False
        [3, 2],            # Pinta 1: 0
        [1]                # Pinta 1: 1 siempre
    ]

    # Contando ases como comodines → 3 apariciones de la pinta 1
    assert contador.contar_en_todos_los_dados(cachos, 1, usar_ases_como_comidines) == 3

    usar_ases_como_comidines = False

    # No contando ases como comodines → 2 apariciones de la pinta 1
    assert contador.contar_en_todos_los_dados(cachos, 1, usar_ases_como_comidines) == 2
