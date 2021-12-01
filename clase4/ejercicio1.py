def preguntar():
    nombre = input('¿Como te llamas? ')
    edad  = input('¿Cuantos años tienes? ')
    anio = (100-int(edad)) + 2021
    print('Hola ',nombre, ' cumpliras 100 años en ', str(anio)  )
    return



preguntar()