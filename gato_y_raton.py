import numpy as np, os, time, random

#definir el tablero

tablero = np.zeros((10,10), dtype=int)

#definimos la posicion del gato y el raton
posicion_actual_gato = [1,1]

posicion_actual_raton = [8,8]

#una funcion para que el raton se mueva aleatoriamente
def movimiento_aleatorio_raton(posicion_actual_raton):
    movimientos = [
        (1,0), #x aumenta en 1, y se queda igual (se mueve a la derecha)
        (-1,0), #x disminuye en 1, y se queda igual (se mueve a la izquierda)
        (0,1), #y aumenta en 1, x se queda igual (se mueve hacia arriba)
        (0,-1), #y disminuye en 1, x se queda igual (se mueve hacia abajo)
        (1,1), #x e y aumentan en 1 (se mueve ariiba a la derecha)
        (1,-1), # x aumenta 1 e y disminuye 1 (se mueve abajo a la derecha)
        (-1,-1), # x e y disminuyen en 1, (se mueve abajo a la izquierda)
        (-1,1) # x disminuye en 1 e y aumenta en 1 (se mueve arriba a la izquerda)
    ]
    random.shuffle(movimientos)

    for mx, my in movimientos: #mx toma el primer elemento de la tupla movimientos (x), y my toma el segundo elemento (y)

        movimiento_x = posicion_actual_raton[0] + mx #sumamos el movimiento en el eje x a la posicion actual del raton
        movimiento_y = posicion_actual_raton[1] + my #sumamos el movimiento en el eje y a la posicion actual del raton

        if tablero[movimiento_x, movimiento_y] != 9:

            return(movimiento_x, movimiento_y)
            
# #una funcion para que el gato persiga linealmente al raton
def gato_persigue_linealmente(posicion_actual_gato, posicion_actual_raton):

    gx, gy = posicion_actual_gato #gx toma el valor de gato[0] y gy toma el valor de gato[1]

    rx, ry = posicion_actual_raton #rx toma el valor de raton[0] y ry toma el valor de raton[1]

    #verifica que si el gato esta en la misma posicion del raton
    if gx == rx and gy  == ry:

        return(gx, gy)
    
    #verifica si el gato esta mas a la derecha del raton para moverlo a la izquierda
    elif gx > rx:
        gx -= 2
    #verifica si el gato esta mas a la izquierda del raton para moverlo a la derecha
    elif gx < rx:
        gx += 2

    #en caso de que el gato este 'sobre'  o 'bajo' el raton, solamente lo movemos arriba o abajo
    else:

        #si el gato esta bajo el raton, lo movemos mas arriba
        if gy > ry:
            gy -= 2

        #si el gato esta sobre el raton lo movemos mas abajo
        elif gy < ry:
            gy += 2
    
    if tablero[gx,gy] == 9:
        return(posicion_actual_gato[0], posicion_actual_gato[1])
    
    return(gx, gy)


while True:

    seleccionar_modo_de_juego = input(f'Ingrese G para jugar como gato\n R para jugar como raton\n o I para ver jugar a la IA')
    jugar_como = seleccionar_modo_de_juego.lower().strip()
    if jugar_como == 'g':
        print('Jugaras como gato.')
        break
    elif jugar_como == 'r':
        print('Jugaras como raton.')
        break
    elif jugar_como == 'i':
        print('Veras a la IA jugar.')
        break
    else:
        print('Valor invalido')

if jugar_como == 'i':
    while True:
        os.system(
            'cls' if os.name == 'nt' 
            else 'clear'
        )

        #definimos los bordes

        tablero[:,:] = 0
        tablero[0,:] = 9
        tablero[9,:] = 9
        tablero[:,0] = 9
        tablero[:,9] = 9
        tablero[4,4] = 9

        #definimos la posicion del raton y del gato

        tablero[ posicion_actual_raton[0] , posicion_actual_raton[1] ] = 1

        tablero[ posicion_actual_gato[0] , posicion_actual_gato[1] ] = 2

        

        for fila in tablero:
            simbolos = []
            for x in fila:
                if x == 9:
                    simbolos.append('🧱')
                elif x == 1:
                    simbolos.append('🐁')
                elif x == 2:
                    simbolos.append('🐈')
                else:
                    simbolos.append('🟨')
            print(' '.join(simbolos))

        nueva_posicion_raton = movimiento_aleatorio_raton(posicion_actual_raton)
        posicion_actual_raton = list(nueva_posicion_raton)

        nueva_posicion_gato = gato_persigue_linealmente(posicion_actual_gato, posicion_actual_raton)
        if nueva_posicion_gato[0] == posicion_actual_raton[0] and nueva_posicion_gato[1] == posicion_actual_raton[1]:
            print('El gato atrapo al raton')
            break
        else:
            posicion_actual_gato = list(nueva_posicion_gato)        
        
        time.sleep(3)



