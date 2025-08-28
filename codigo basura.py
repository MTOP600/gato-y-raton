codigo basura

# #una funcion para que el gato persiga linealmente al raton
def gato_persigue_linealmente(posicion_actual_gato, posicion_actual_raton):

    gx, gy = posicion_actual_gato #gx toma el valor de gato[0] y gy toma el valor de gato[1]

    rx, ry = posicion_actual_raton #rx toma el valor de raton[0] y ry toma el valor de raton[1]

    #verifica que si el gato esta en la misma posicion del raton
    if gx == rx and gy  == ry:
        return(False)
    
    #verifica si el gato esta mas a la derecha del raton para moverlo a la izquierda
    elif posicion_actual_gato[0] > posicion_actual_raton[0]:
        posicion_actual_gato[0] -= 2
    #verifica si el gato esta mas a la izquierda del raton para moverlo a la derecha
    elif posicion_actual_gato[0] < posicion_actual_raton[0]:
        posicion_actual_gato[0] += 2

    #en caso de que el gato este 'sobre'  o 'bajo' el raton, solamente lo movemos arriba o abajo
    else:

        #si el gato esta bajo el raton, lo movemos mas arriba
        if posicion_actual_gato[1] > posicion_actual_raton[1]:
            posicion_actual_gato[1] -= 2

        #si el gato esta sobre el raton lo movemos mas abajo
        elif posicion_actual_gato[1] < posicion_actual_raton[1]:
            posicion_actual_gato[1] += 2