import pytest
from src.juego.gestor_partida import GestorPartida
from src.utils.dudo_types import ResultadoDudo, TipoResultado


class TestGestorPartida:
    """
    Suite de tests para la clase GestorPartida.
    Verifica el correcto funcionamiento del gestor en todos los aspectos de la partida:
    inicialización, manejo de turnos, procesamiento de acciones y detección de fin de juego.
    """

    def test_inicializa_jugadores_con_cinco_dados_cada_uno(self):
        """
        Verifica que el gestor inicialice correctamente a todos los jugadores
        con la cantidad estándar de 5 dados cada uno.
        """

        jugadores = ["Juan", "Maria", "Pedro"]

        gestor = GestorPartida(jugadores)

        assert gestor.obtener_dados_jugador("Juan") == 5
        assert gestor.obtener_dados_jugador("Maria") == 5
        assert gestor.obtener_dados_jugador("Pedro") == 5

    def test_actualiza_dados_cuando_jugador_pierde(self):
        """
        Verifica que el gestor actualice correctamente la cantidad de dados
        cuando un jugador pierde una ronda.
        """

        jugadores = ["Juan", "Maria"]
        gestor = GestorPartida(jugadores)

        # Verificar estado inicial
        assert gestor.obtener_dados_jugador("Juan") == 5

        gestor.quitar_dado_jugador("Juan")

        # Juan ahora debe tener 4 dados, Maria sigue con 5
        assert gestor.obtener_dados_jugador("Juan") == 4
        assert gestor.obtener_dados_jugador("Maria") == 5

    def test_determina_quien_inicia_siguiente_ronda(self):
        """
        Verifica que el gestor establezca correctamente quién debe iniciar
        la siguiente ronda basándose en quién perdió la ronda anterior.
        """

        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        # establecer a Juan como perdedor de la ronda
        gestor.establecer_perdedor_ronda("Juan")

        # Juan debe ser quien inicia la siguiente ronda
        assert gestor.obtener_iniciador_ronda() == "Juan"

    def test_detecta_cuando_jugador_tiene_un_solo_dado(self):
        """
        Verifica que el gestor detecte correctamente cuando un jugador
        se queda con un solo dado (condición especial en las reglas).
        """

        # gestor con jugadores inicializados
        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        # Juan pierde 4 dados (le quedan 4 intentos de quitar dados)
        for _ in range(4):
            gestor.quitar_dado_jugador("Juan")

        # verificar si Juan tiene un solo dado
        tiene_un_dado = gestor.tiene_jugador_un_solo_dado("Juan")

        #  debe detectar que Juan tiene un solo dado
        assert tiene_un_dado == True

        #  los demás jugadores siguen con 5 dados
        assert gestor.tiene_jugador_un_solo_dado("Maria") == False
        assert gestor.tiene_jugador_un_solo_dado("Pedro") == False

    def test_maneja_flujo_de_turnos(self):
        """
        Verifica que el gestor maneje correctamente el flujo de turnos
        en orden secuencial y cíclico entre los jugadores.
        """

        # gestor con jugadores en orden específico
        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        #  verificar la secuencia de turnos cíclica
        assert gestor.obtener_jugador_actual() == "Juan" # primer turno de juan

        gestor.avanzar_turno()
        assert gestor.obtener_jugador_actual() == "Maria"

        gestor.avanzar_turno()
        assert gestor.obtener_jugador_actual() == "Pedro"

        gestor.avanzar_turno()
        assert gestor.obtener_jugador_actual() == "Juan" # vuelve a Juan (cíclico)

    def test_detecta_fin_del_juego(self):
        """
        Verifica que el gestor detecte correctamente el fin del juego
        cuando solo queda un jugador activo.
        """
        #  gestor con 3 jugadores
        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        # Verificar estado inicial (juego no ha terminado)
        assert gestor.es_fin_del_juego() == False
        assert gestor.obtener_ganador() is None

        #  eliminar completamente a Juan y Pedro (5 dados cada uno)
        for _ in range(5):
            gestor.quitar_dado_jugador("Juan") # elimina juan
            gestor.quitar_dado_jugador("Pedro") #elimina pedro

        #  debe detectar fin del juego con Maria como ganadora
        assert gestor.es_fin_del_juego() == True
        assert gestor.obtener_ganador() == "Maria"

    def test_establecer_direccion_de_turnos(self):
        """
        Verifica que el gestor permita cambiar la dirección de los turnos
        entre sentido horario y antihorario.
        """
        # gestor iniciando con Juan
        jugadores = ["Juan", "Maria", "Pedro"]
        gestor = GestorPartida(jugadores)

        # avanzar en dirección horaria (por defecto)
        gestor.avanzar_turno()
        assert gestor.obtener_jugador_actual() == "Maria"

        # cambiar a dirección antihoraria
        gestor.establecer_direccion(False)
        gestor.avanzar_turno()

        # debe volver a Juan (retroceso)
        assert gestor.obtener_jugador_actual() == "Juan"


### Tests usando mocker para los casos que necesiten ser determinista
def test_procesar_dudo_cuando_dudador_pierde(mocker):
    """
    Verifica que el gestor procese correctamente un dudo cuando el dudador pierde.
    Utiliza mocking para hacer el test determinista.
    """
    #  gestor con 2 jugadores y resultado de dudo mockeado
    jugadores = ["Juan", "Maria"]
    gestor = GestorPartida(jugadores)

    # Mock del resultado donde el dudador pierde
    mock_resultado = ResultadoDudo(
        apuesta_es_cierta=True,
        quien_pierde=TipoResultado.DUDADOR,
        dados_reales=4,
        dados_apostados=3
    )
    mocker.patch.object(gestor._arbitro, "determinar_resultado_dudo", return_value=mock_resultado)

    # Juan hace una apuesta y Maria la duda
    gestor.realizar_apuesta("Juan", 3, 4)
    resultado = gestor.procesar_dudo("Maria")

    # verificar que el resultado es correcto
    assert resultado["apuesta_es_cierta"] is True
    assert resultado["quien_pierde"] == "dudador"
    assert resultado["perdedor"] == "Maria"
    assert gestor.obtener_dados_jugador("Maria") == 4
    assert gestor.obtener_dados_jugador("Juan") == 5
    assert gestor.obtener_iniciador_ronda() == "Maria"


def test_iniciar_partida_determina_iniciador(mocker):
    """
    Verifica que el gestor determine correctamente el iniciador de la partida
    mediante lanzamiento de dados. Utiliza mocking para hacer el test determinista.
    """
    #  gestor con 3 jugadores y tiradas predefinidas
    jugadores = ["Juan", "Maria", "Pedro"]
    gestor = GestorPartida(jugadores)

    tiradas_deseadas = [3, 5, 2]  # juan, maria y Pedro

    #  mockear random.randint para devolver las tiradas en orden
    mocker.patch("random.randint", side_effect=tiradas_deseadas)

    resultado = gestor.iniciar_partida()

    #  Maria debe ser la iniciadora por tener la tirada más alta (5)
    assert resultado["iniciador"] == "Maria"
    assert gestor._iniciador_ronda == "Maria"
    assert gestor.obtener_jugador_actual() == "Maria"



