#JUEGO DE ADIVINA EL NUMERO
#EL PROGRAMA GENERA UN NUMERO ALEATRIOO ENTRE 1 Y 7, Y EL USUARIO DEBE ADIVINAR, EL PROGRAMA LE DARA PISTAS SI ES MAYO
import random
numero_aleatorio = random.randint(1, 100)
while True:
        try:
            numero_ingresado = int(input('Ingrese un numero entre 1 y 100  '))
            if numero_aleatorio == numero_ingresado:
                print('Adinvinaste')
                break
            elif numero_ingresado < numero_aleatorio:
                print('El numero debe ser mayor')
            elif numero_ingresado > numero_aleatorio:
                print('El numero debe ser menor')
        except ValueError:
             print('Ingrese un numero entero, TONTO')
 