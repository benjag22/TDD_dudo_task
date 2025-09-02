import pytest
from src.juego.arbitro_ronda import ArbitroRonda
from src.utils.dudo_types import TipoResultado, Apuesta


class TestArbitroRonda:
    """
    Suite de tests para la clase ArbitroRonda.
    Verifica el correcto funcionamiento del árbitro en las acciones de dudo y calzar.
    """
    
    def test_determina_apuesta_falsa_cuando_hay_menos_dados_de_los_apostados(self):
        """
        Verifica que el árbitro determine correctamente una apuesta falsa cuando
        no hay suficientes dados de la pinta apostada.
        """
        #  dados con solo 2 trenes (3) y sin ases como comodines
        todos_los_cachos = [3, 3, 1, 2, 4, 5, 6]
        apuesta = Apuesta(cantidad=3, pinta=3, jugador="Jugador cualquiera")  # 3 trenes

        arbitro = ArbitroRonda()
        
        #  determinar resultado del dudo
        resultado = arbitro.determinar_resultado_dudo(apuesta, [todos_los_cachos],usar_ases_como_comodines = False)
        
        #  la apuesta es falsa (hay solo 2 trenes, no 3)
        assert resultado.apuesta_es_cierta == False
        assert resultado.quien_pierde == TipoResultado.APOSTADOR

    def test_calzar_exitoso_cuando_apuesta_es_exacta(self):
        """
        Verifica que el árbitro determine un calzar exitoso cuando
        la cantidad de dados coincide exactamente con la apuesta.
        """

        #  dados con exactamente 3 trenes (3) y sin ases como comodines
        todos_los_cachos = [3, 3, 3, 1, 2]
        apuesta = Apuesta(cantidad=3, pinta=3, jugador="Jugador cualquiera")  # 3 trenes

        arbitro = ArbitroRonda()
        
        #  determinar resultado del calzar
        resultado = arbitro.determinar_resultado_calzar(apuesta, [todos_los_cachos], usar_ases_como_comodines = False)
        
        #  calce exitoso (hay exactamente 3 trenes)
        assert resultado.calce_exitoso == True
        assert resultado.quien_gana_dado == "calzador"

    def test_valida_condiciones_calzar(self):
        """
        Verifica que el árbitro valide correctamente las condiciones para realizar un calzar.
        """
        #  jugador con 3 dados de un total de 10 dados en juego
        total_dados_en_juego = 10
        dados_del_jugador = 3
        
        arbitro = ArbitroRonda()
        
        #  validar condiciones para calzar
        puede_calzar = arbitro.validar_condiciones_calzar(dados_del_jugador, total_dados_en_juego)
        
        #  No puede calzar (tiene menos de la mitad de dados y más de 1 dado)
        assert puede_calzar == False