# Ejercicio 2: Preguntar al usuario un número y mostrar si es par o impar. Si el número es
# múltiplo de 4 imprimir el mensaje apropiado al usuario.

def preguntar():
    n = input('Dime un número: ')
    if (int(n) % 2) == 0:
        print('El numero',n, 'es par')
    else:
        print('El numero',n, 'es impar')

    if (int(n) % 4) == 0:
        print('El numero',n, 'es multiplo de 4')
    else:
        print('El numero',n, 'no es multiplo de 4')

preguntar()    