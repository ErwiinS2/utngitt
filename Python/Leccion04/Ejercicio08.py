# Ejercicio 8 - Cajero automatico
# Hacer un programa qeu simule un cajero automatico con un saldo inicial de $1000
# y tenga el siguiente menu de opciones
# Ingresar dinero en la cuenta
# Retirar dinero de la cuenta
# Mostrar el dinero disponible
# Salir

saldo = 1000
while True:
    print('MENU'
          '\n1. Ingresar dinero en la cuenta'
          '\n2. Retirar dinero de la cuenta'
          '\n3. Mostrar dinero disponible'
          '\n4.Salir')
    opcion = int(input('Seleccione una opcion: '))
    if opcion == 1:
        monto = float(input('Digite el monto que desea ingresar: '))
        saldo += monto
        print(f'El saldo actual es: {saldo}')
    elif opcion == 2:
        monto = float(input('Digite el monto que desea retirar: '))
        if monto <= saldo:
            saldo -= monto
            print(f'El saldo actual es: {saldo}')
        else:
            print('El saldo no es suficiente.')
    elif opcion == 3:
        print(f'El dinero disponible es de: ${saldo}')
    elif opcion == 4:
        print('Gracias por utilizar el cajero. Hasta pronto')
        break
    else:
        print('Por favor ingrese una opción válida')