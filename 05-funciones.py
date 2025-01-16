import os

'''def funcion1():
    os.system('clear')
    num1 = int(input('numero 1: '))
    num2 = int(input('numero 2: '))
    res = num1 + num2
    print(f'resultado = {res}')

def funcion2():
    print('soy la funcion 2')
'''

def suma(a, b):
    res = a + b
    print(f'el resultado es: {res}')

def resta(a, b):
    res = a - b
    print(f'el resultado es: {res}')

def mult(a, b):
    res = a * b
    print(f'el resultado es: {res}')

def div(a, b):
    res = a / b
    print(f'el resultado es: {res}')


def run():
    os.system('clear')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Salir')
    opcion = int(input('opcion: '))
    
    while(opcion != 5):
        os.system('clear')
        num1 = int(input('numero 1: '))
        num2 = int(input('numero 2: '))
        if (opcion == 1):
            suma(num1, num2)
        if (opcion == 2):
            resta(num1, num2)
        if (opcion == 3):
            mult(num1, num2)
        if (opcion == 4):
            div(num1, num2)

        print('')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        print('5. Salir')
        opcion = int(input('Ingresa una opcion: '))

if __name__ == '__main__':
    run()