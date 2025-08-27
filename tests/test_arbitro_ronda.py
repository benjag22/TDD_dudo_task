import pytest
from src.juego.arbitro_ronda import ArbitroRonda


class TestArbitroRonda:
    
    def test_determina_apuesta_falsa_cuando_hay_menos_dados_de_los_apostados(self):

        todos_los_dados = [3, 3, 1, 2, 4, 5, 6]
        apuesta = {"cantidad": 3, "pinta": 3}  # 3 trenes
        
        arbitro = ArbitroRonda()
        
        resultado = arbitro.determinar_resultado_dudo(apuesta, todos_los_dados)
        
        # Assert: la apuesta es falsa (hay solo 2 trenes, no 3)
        assert resultado["apuesta_es_cierta"] == False
        assert resultado["quien_pierde"] == "apostador"

    def test_calzar_exitoso_cuando_apuesta_es_exacta(self):

        todos_los_dados = [3, 3, 3, 1, 2]
        apuesta = {"cantidad": 3, "pinta": 3}  # 3 trenes

        arbitro = ArbitroRonda()
        
        resultado = arbitro.determinar_resultado_calzar(apuesta, todos_los_dados)
        
        # Assert: calce exitoso (hay exactamente 3 trenes)
        assert resultado["calce_exitoso"] == True
        assert resultado["quien_gana_dado"] == "calzador"