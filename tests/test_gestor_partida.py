import pytest
from src.juego.gestor_partida import GestorPartida


class TestGestorPartida:
    
    def test_inicializa_jugadores_con_cinco_dados_cada_uno(self):

        jugadores = ["Juan", "Maria", "Pedro"]

        gestor = GestorPartida(jugadores)
        
        # Assert: cada jugador debe tener 5 dados
        assert gestor.obtener_dados_jugador("Juan") == 5
        assert gestor.obtener_dados_jugador("Maria") == 5
        assert gestor.obtener_dados_jugador("Pedro") == 5