# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un numero por teclado y guarde en unalista su tabla de multiplicar hasta el 10 por ejemplo
# si digita 5 la lista tendra : 5-10-15-20-25-30,35,40,45,50,55,60,65,70,75,80,85, 90, 95, 50
numero = int(input('Digite un numero: '))
lista = []
for i in range(1, 11):
    lista.append(i*numero)

print(f'\nTabla de multiplicar del numero {numero}: \n{lista}')

for indice, i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}') # Este ciclo es para ver el formato de tabla de multiplicar