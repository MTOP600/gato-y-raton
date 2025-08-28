def gato_con_memoria(tablero, posicion_actual_gato, posicion_actual_raton, historial_gato):
    movimientos_posibles = movimientos_posibles_gato(tablero, posicion_actual_gato)
    
    # Filtrar movimientos que no estén en el historial reciente
    movimientos_sin_repetir = []
    for mov in movimientos_posibles:
        if mov not in historial_gato[-3:]:  # Evitar últimas 3 posiciones
            movimientos_sin_repetir.append(mov)
    
    # Si todos los movimientos están en el historial, usar movimiento aleatorio
    if not movimientos_sin_repetir:
        movimientos_sin_repetir = movimientos_posibles
    
    mejor_movimiento = posicion_actual_gato
    mejor_distancia = float('inf')
    
    for movimiento in movimientos_sin_repetir:
        distancia = calcular_distancia_manhhattan(movimiento, posicion_actual_raton)
        if distancia < mejor_distancia:
            mejor_distancia = distancia
            mejor_movimiento = movimiento
    
    return mejor_movimiento

# Agregar al bucle principal:
historial_gato = []

# En cada iteración:
nueva_posicion_gato = gato_con_memoria(tablero, posicion_actual_gato, posicion_actual_raton, historial_gato)
historial_gato.append(posicion_actual_gato)
if len(historial_gato) > 5:
    historial_gato.pop(0)