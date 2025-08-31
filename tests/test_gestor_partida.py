import pytest
from src.juego.gestor_partida import GestorPartida
from src.utils.dudo_types import ResultadoDudo, TipoResultado


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

    def test_determina_quien_inicia_siguiente_ronda(self):

        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        gestor.establecer_perdedor_ronda("Juan")

        # Assert: Juan debe ser quien inicia la siguiente ronda
        assert gestor.obtener_iniciador_ronda() == "Juan"

    def test_detecta_cuando_jugador_tiene_un_solo_dado(self):

        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        for _ in range(4):
            gestor.quitar_dado_jugador("Juan")

        tiene_un_dado = gestor.tiene_jugador_un_solo_dado("Juan")

        # Assert: debe detectar que Juan tiene un solo dado
        assert tiene_un_dado == True

        assert gestor.tiene_jugador_un_solo_dado("Maria") == False
        assert gestor.tiene_jugador_un_solo_dado("Pedro") == False

    def test_maneja_flujo_de_turnos(self):

        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        # Assert: verificar la secuencia de turnos
        assert gestor.obtener_jugador_actual() == "Juan" #primer turno de juan

        gestor.avanzar_turno()
        assert gestor.obtener_jugador_actual() == "Maria"

        gestor.avanzar_turno()
        assert gestor.obtener_jugador_actual() == "Pedro"

        gestor.avanzar_turno()
        assert gestor.obtener_jugador_actual() == "Juan"

    def test_detecta_fin_del_juego(self):
        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        assert gestor.es_fin_del_juego() == False
        assert gestor.obtener_ganador() is None

        for _ in range(5):
            gestor.quitar_dado_jugador("Juan") # elimina juan
            gestor.quitar_dado_jugador("Pedro") #elimina pedro

        assert gestor.es_fin_del_juego() == True
        assert gestor.obtener_ganador() == "Maria"

    def test_establecer_direccion_de_turnos(self):
        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        gestor.avanzar_turno()
        assert gestor.obtener_jugador_actual() == "Maria"

        gestor.establecer_direccion(False)
        gestor.avanzar_turno()
        assert gestor.obtener_jugador_actual() == "Juan"

### Tests usando mocker para los casos que necesiten ser determinista
def test_procesar_dudo_cuando_dudador_pierde(mocker):
    # Arrange
    jugadores = ["Juan", "Maria"]
    gestor = GestorPartida(jugadores)

    mock_resultado = ResultadoDudo(
        apuesta_es_cierta=True,
        quien_pierde=TipoResultado.DUDADOR,
        dados_reales=4,
        dados_apostados=3
    )
    mocker.patch.object(gestor.arbitro, "determinar_resultado_dudo", return_value=mock_resultado)

    # Act
    gestor.realizar_apuesta("Juan", 3, 4)
    resultado = gestor.procesar_dudo("Maria")

    # Assert
    assert resultado["apuesta_es_cierta"] is True
    assert resultado["quien_pierde"] == "dudador"
    assert resultado["perdedor"] == "Maria"
    assert gestor.obtener_dados_jugador("Maria") == 4  # Perdió un dado
    assert gestor.obtener_dados_jugador("Juan") == 5  # Juan mantiene sus dados
    assert gestor.obtener_iniciador_ronda() == "Maria"  # Maria inicia la próxima ronda


def test_iniciar_partida_determina_iniciador(mocker):
    jugadores = ["Juan", "Maria", "Pedro"]
    gestor = GestorPartida(jugadores)

    tiradas_deseadas = [3, 5, 2]  # juan, maria y Pedro

    # mock random.randint para devolver las tiradas en orden
    mocker.patch("random.randint", side_effect=tiradas_deseadas)

    resultado = gestor.iniciar_partida()

    assert resultado["iniciador"] == "Maria"
    assert gestor.iniciador_ronda == "Maria"
    assert gestor.obtener_jugador_actual() == "Maria"


