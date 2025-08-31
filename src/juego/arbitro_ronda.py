from src.juego.contador_pintas import ContadorPintas
from src.utils.dudo_types import ResultadoDudo, ResultadoCalzar, TipoResultado, Apuesta
class ArbitroRonda:
    contador_pintas: ContadorPintas

    def __init__(self) -> None:
        self.contador_pintas = ContadorPintas()

    def determinar_resultado_dudo(self, apuesta: Apuesta,
                                  todos_los_cachos: list[list[int]],
                                  usar_ases_como_comodines: bool = True) -> ResultadoDudo:

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
        if dados_del_jugador == 1:
            return True

        mitad_dados = total_dados_en_juego / 2
        if dados_del_jugador >= mitad_dados:
            return True

        return False
