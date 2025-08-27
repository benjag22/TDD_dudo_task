class ArbitroRonda:
    
    def determinar_resultado_dudo(self, apuesta, todos_los_dados):
        
        cantidad_apostada = apuesta["cantidad"]
        pinta_apostada = apuesta["pinta"]
        
        dados_encontrados = todos_los_dados.count(pinta_apostada)

        apuesta_es_cierta = dados_encontrados >= cantidad_apostada #se verifica la apuesta

        if apuesta_es_cierta:
            quien_pierde = "dudador"
        else:
            quien_pierde = "apostador"

        return {
            "apuesta_es_cierta": apuesta_es_cierta,
            "quien_pierde": quien_pierde
        }