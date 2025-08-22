import numpy as np
import os, time
import random



tamano_tablero = 10
tablero = np.zeros((tamano_tablero,tamano_tablero), dtype=int)
tablero[0,:] = 9
tablero[9,:] = 9
tablero[:,0] = 9
tablero[:,9] = 9

print(tablero)
raton = [5,7]
gato = [4,4]



while True:
    os.system('cls' if os.name == 'nt' else 'clear')


    tablero[:, :] = 0
    tablero[0,:] = 9
    tablero[9,:] = 9
    tablero[:,0] = 9
    tablero[:,9] = 9

    tablero[raton[0], raton[1]] = 1
    tablero[gato[0], gato [1]] = 2

    for fila in tablero:
        simbolos = []
        for x in fila:
            if x == 1:
                simbolos.append('R')
            elif x == 2:
                simbolos.append('G')
            elif x == 9:
                simbolos.append('H')
            else:
                simbolos.append('.')
            
        print(' '.join(simbolos))

    #---MOVIMIENTO DEL RATON

    movimientos = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1), (1,-1), (-1,1)]
    random.shuffle(movimientos)

    for dx, dy in movimientos:
        movimiento_x = raton[0] + dx
        movimiento_y = raton[1] + dy
        if tablero[movimiento_x, movimiento_y] != 9:
            raton[0] = movimiento_x
            raton[1] = movimiento_y
            break

    # if raton[0] 
    #     nueva_posicion_raton_x = random.randint( (raton[0]), (raton[0]+1) )
    # elif raton[0] >= (tamano_tablero-2):
    #     nueva_posicion_raton_x = random.randint( ( raton[0] -1 ), (raton[0]) )
    # elif raton[1] <= 1:
    #     nueva_posicion_raton_y = random.randint( (raton[1]), (raton[1]+1) )
    # elif raton[1] >= (tamano_tablero-2):
    #     nueva_posicion_raton_y = random.randint( ( raton[1] -1 ), (raton[1]) )
    # else:
    #     nueva_posicion_raton_x = random.randint( (raton[0] -1 ) , (raton[0] +1))
    #     nueva_posicion_raton_y = random.randint( (raton[1] -1 ) , (raton[1] +1))
        
    # nueva_posicion_raton_x = random.randint((raton[0]-1),(raton[0]-1))
    # nueva_posicion_raton_y = random.randint((raton[1]-1),(raton[1]-1))
    # raton[0] = nueva_posicion_raton_x
    # raton[1] = nueva_posicion_raton_y<= 1:

    #---MOVIMIENTO DEL GATO
    # if gato[0] == raton[0] and gato[1] == raton[1]:
    #     print('El gato atrapo al raton')
    #     break

    # elif gato[0] > raton[0]:
    #     gato[0] -= 1

    # elif gato[0] < raton[0]:
    #     gato[0] += 1

    # elif gato[1] > raton[1]:
    #     gato[1] -= 1

    # elif gato[1] < raton[1]:
    #     gato[1] += 1

    # elif gato[1] == raton[1]:
    #     gato[1] = raton[1]

    # elif gato[1] == raton[1]:
    #     gato[1] = raton[1]

    if gato[0] == raton[0] and gato[1] == raton[1]:
        print('El gato atrapo al raton')
        
        break

    elif gato[0] < raton[0]:
        gato[0] += 2
    elif gato[0] > raton[0]:
        gato[0] -= 2
    else:
        if gato[1] < raton[1]:
            gato[1] += 2
        elif gato[1] > raton[1]:
            gato[1] -= 2

    time.sleep(2)
