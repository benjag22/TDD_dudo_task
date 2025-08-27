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

    def test_actualiza_dados_cuando_jugador_pierde(self):
        
        jugadores = ["Juan", "Maria"]
        gestor = GestorPartida(jugadores)
        
        assert gestor.obtener_dados_jugador("Juan") == 5
        
        gestor.quitar_dado_jugador("Juan")
        
        # Assert: Juan ahora debe tener 4 dados
        assert gestor.obtener_dados_jugador("Juan") == 4
        assert gestor.obtener_dados_jugador("Maria") == 5