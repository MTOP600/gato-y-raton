# Agregar variable global para memoria
posicion_anterior_gato = None

# Función modificada del gato con memoria
def gato_con_memoria(tablero, posicion_actual_gato, posicion_actual_raton, posicion_anterior):
    movimientos_posibles = movimientos_posibles_gato(tablero, posicion_actual_gato)
    
    # Filtrar posición anterior
    if posicion_anterior:
        movimientos_posibles = [mov for mov in movimientos_posibles if mov != tuple(posicion_anterior)]
    
    # Si no quedan movimientos, usar todos
    if not movimientos_posibles:
        movimientos_posibles = movimientos_posibles_gato(tablero, posicion_actual_gato)
    
    mejor_movimiento = posicion_actual_gato
    mejor_distancia = float('inf')
    
    for movimiento in movimientos_posibles:
        distancia = calcular_distancia_manhhattan(movimiento, posicion_actual_raton)
        if distancia < mejor_distancia:
            mejor_distancia = distancia
            mejor_movimiento = movimiento
    
    return mejor_movimiento

# En el bucle principal, cambiar:
# ANTES:
# nueva_posicion_gato = gato_persigue_linealmente(tablero, posicion_actual_gato, posicion_actual_raton)

# DESPUÉS:
nueva_posicion_gato = gato_con_memoria(tablero, posicion_actual_gato, posicion_actual_raton, posicion_anterior_gato)
posicion_anterior_gato = posicion_actual_gato.copy()  # Guardar posición actual como anterior
posicion_actual_gato = list(nueva_posicion_gato)