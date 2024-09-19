# Ejercicio 7: Juego adivina el numero
# Realizr un juego para adivinar un numero. Para ello se debe generar un numero aleatorio entre 1 y 100
# y luego it pidinedo numeros indicando es "mayor" " es menor" segun sea mayor o menor con respecto a N
# El proceso termina cuando el usuario acierta y alli se debe mostrar el numero de intentos

import random
print("\t.:Juego adivina el numero:.")
aleatorio = random.randint(0,100) # Toma del 0 al 100 literal, generamos un numero aleatorio
contador = 0
while True:
    numero = int(input('Digite un numero: '))
    contador += 1
    if numero > aleatorio:
        print("\t No es el numero. Digita un numero menor")
    elif numero < aleatorio:
        print("\t No es el numero. Digite un numero mayor")
    else:
        print(f'FELICIDADES acabas de adivinar el numero: {aleatorio}')
        break # Rompe el ciclo y el bucle
print(f"\n Numero de intentos: {contador}")