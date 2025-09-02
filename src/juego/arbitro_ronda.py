from src.juego.contador_pintas import ContadorPintas
from src.utils.dudo_types import ResultadoDudo, ResultadoCalzar, TipoResultado, Apuesta

class ArbitroRonda:
    """
    Clase que actúa como árbitro en las rondas del juego de Dudo.
    Se encarga de determinar los resultados de las acciones "dudo" y "calzar",
    validando las condiciones especiales y contando los dados correspondientes.
    """
    
    contador_pintas: ContadorPintas

    def __init__(self) -> None:
        """
        Inicializa el árbitro con un contador de pintas para evaluar los dados.
        """
        self.contador_pintas = ContadorPintas()

    def determinar_resultado_dudo(self, apuesta: Apuesta,
                                  todos_los_cachos: list[list[int]],
                                  usar_ases_como_comodines: bool = True) -> ResultadoDudo:
        """
        Determina el resultado de una acción "dudo" comparando la apuesta con los dados reales.
        
        Args:
            apuesta (Apuesta): La apuesta que se está dudando (cantidad, pinta, jugador).
            todos_los_cachos (list[list[int]]): Lista de todos los dados de todos los jugadores.
            usar_ases_como_comodines (bool, optional): Si los ases (1) cuentan como comodines.
                                                      Por defecto es True.
        
        Returns:
            ResultadoDudo: Objeto con el resultado del dudo, incluyendo quién pierde y dados contados.
        """

        dados_encontrados = self.contador_pintas.contar_en_todos_los_dados(
            todos_los_cachos,
            pinta=apuesta.pinta,
            usar_ases_como_comodines=usar_ases_como_comodines
        )

        apuesta_es_cierta = dados_encontrados >= apuesta.cantidad

        quien_pierde = TipoResultado.DUDADOR if apuesta_es_cierta else TipoResultado.APOSTADOR

        return ResultadoDudo(
            apuesta_es_cierta=apuesta_es_cierta,
            quien_pierde=quien_pierde,
            dados_reales=dados_encontrados,
            dados_apostados=apuesta.cantidad
        )

    def determinar_resultado_calzar(self,
                                    apuesta: Apuesta,
                                    todos_los_cachos: list[list[int]],
                                    usar_ases_como_comodines: bool = True
                                    ) -> ResultadoCalzar:
        """
        Determina el resultado de una acción "calzar" verificando si la apuesta es exactamente correcta.
        
        Args:
            apuesta (Apuesta): La apuesta que se está calzando (cantidad, pinta, jugador).
            todos_los_cachos (list[list[int]]): Lista de todos los dados de todos los jugadores.
            usar_ases_como_comodines (bool, optional): Si los ases (1) cuentan como comodines.
                                                      Por defecto es True.
        
        Returns:
            ResultadoCalzar: Objeto con el resultado del calzar, incluyendo si fue exitoso y quién gana.
        """
        dados_encontrados = self.contador_pintas.contar_en_todos_los_dados(
            todos_los_cachos, apuesta.pinta, usar_ases_como_comodines
        )

        calce_exitoso = dados_encontrados == apuesta.cantidad
        quien_gana_dado = "calzador" if calce_exitoso else None

        return ResultadoCalzar(
            calce_exitoso=calce_exitoso,
            quien_gana_dado=quien_gana_dado,
            dados_reales=dados_encontrados,
            dados_apostados=apuesta.cantidad
        )

    @staticmethod
    def validar_condiciones_calzar(dados_del_jugador: int, total_dados_en_juego: int) -> bool:
        """
        Valida si un jugador puede realizar la acción "calzar" según las reglas del juego.
        
        Reglas:
        - Si el jugador tiene un solo dado, siempre puede calzar.
        - Si el jugador tiene la mitad o más de los dados totales en juego, puede calzar.
        
        Args:
            dados_del_jugador (int): Cantidad de dados que tiene el jugador.
            total_dados_en_juego (int): Total de dados de todos los jugadores activos.
        
        Returns:
            bool: True si el jugador puede calzar, False en caso contrario.
        """
        if dados_del_jugador == 1:
            return True

        mitad_dados = total_dados_en_juego / 2
        if dados_del_jugador >= mitad_dados:
            return True

        return False
