from collections import deque

def gato_con_bfs(tablero, posicion_actual_gato, posicion_actual_raton):
    movimientos_posibles = movimientos_posibles_gato(tablero, posicion_actual_gato)
    
    mejor_movimiento = posicion_actual_gato
    mejor_distancia_real = float('inf')
    
    for movimiento in movimientos_posibles:
        # Calcular distancia real usando BFS
        distancia_real = bfs_distancia(movimiento, posicion_actual_raton, tablero)
        if distancia_real < mejor_distancia_real:
            mejor_distancia_real = distancia_real
            mejor_movimiento = movimiento
    
    return mejor_movimiento

def bfs_distancia(inicio, objetivo, tablero):
    if inicio == objetivo:
        return 0
    
    cola = deque([(inicio, 0)])
    visitadas = {inicio}
    
    while cola:
        (pos_actual, distancia) = cola.popleft()
        
        # Movimientos básicos (no de 2 en 2)
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nueva_x = pos_actual[0] + dx
            nueva_y = pos_actual[1] + dy
            nueva_pos = (nueva_x, nueva_y)
            
            if (0 <= nueva_x < 10 and 0 <= nueva_y < 10 and 
                tablero[nueva_x, nueva_y] != 9 and nueva_pos not in visitadas):
                
                if nueva_pos == objetivo:
                    return distancia + 1
                
                visitadas.add(nueva_pos)
                cola.append((nueva_pos, distancia + 1))
    
    return float('inf')  # No hay camino