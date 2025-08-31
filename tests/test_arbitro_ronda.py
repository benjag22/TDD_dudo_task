import pytest
from src.juego.arbitro_ronda import ArbitroRonda
from src.utils.dudo_types import TipoResultado, Apuesta


class TestArbitroRonda:
    
    def test_determina_apuesta_falsa_cuando_hay_menos_dados_de_los_apostados(self):

        todos_los_cachos = [3, 3, 1, 2, 4, 5, 6]
        apuesta = Apuesta(cantidad=3, pinta=3)  # 3 trenes

        arbitro = ArbitroRonda()
        
        resultado = arbitro.determinar_resultado_dudo(apuesta, [todos_los_cachos],usar_ases_como_comodines = False)
        
        # Assert: la apuesta es falsa (hay solo 2 trenes, no 3)
        assert resultado.apuesta_es_cierta == False
        assert resultado.quien_pierde == TipoResultado.APOSTADOR

    def test_calzar_exitoso_cuando_apuesta_es_exacta(self):

        todos_los_cachos = [3, 3, 3, 1, 2]
        apuesta = Apuesta(cantidad=3, pinta=3)  # 3 trenes

        arbitro = ArbitroRonda()
        
        resultado = arbitro.determinar_resultado_calzar(apuesta, [todos_los_cachos], usar_ases_como_comodines = False)
        
        # Assert: calce exitoso (hay exactamente 3 trenes)
        assert resultado.calce_exitoso == True
        assert resultado.quien_gana_dado == "calzador"

    def test_valida_condiciones_calzar(self):
        
        total_dados_en_juego = 10
        dados_del_jugador = 3
        
        arbitro = ArbitroRonda()
        
        puede_calzar = arbitro.validar_condiciones_calzar(dados_del_jugador, total_dados_en_juego)
        
        # Assert: No puede calzar
        assert puede_calzar == False