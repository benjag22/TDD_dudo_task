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
    
    def determinar_resultado_calzar(self, apuesta, todos_los_dados):
       
        cantidad_apostada = apuesta["cantidad"]
        pinta_apostada = apuesta["pinta"]
        
        dados_encontrados = todos_los_dados.count(pinta_apostada)
        
        calce_exitoso = dados_encontrados == cantidad_apostada
        
        if calce_exitoso:
            quien_gana_dado = "calzador"
        else:
            quien_gana_dado = "apostador"

        return {
            "calce_exitoso": calce_exitoso,
            "quien_gana_dado": quien_gana_dado
        }

    def validar_condiciones_calzar(self, dados_del_jugador, total_dados_en_juego):
       
        # Condicion 1 tiene un solo dado (caso especial)
        if dados_del_jugador == 1:
            return True

        # Condicion 2 tiene la mitad o más de los dados en juego
        mitad_dados = total_dados_en_juego / 2
        if dados_del_jugador >= mitad_dados:
            return True
        
        # No cumple ninguna condicion
        return False