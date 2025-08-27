import pytest
from src.juego.cacho import Cacho


def test_cacho_contiene_5_dados():
    cacho = Cacho()
    assert len(cacho.dados) == 5

