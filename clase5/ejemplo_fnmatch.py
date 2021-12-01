import fnmatch
import os

patron = 'ejemplo*.py'
print('Patron:', patron)

ficheros = os.listdir('.')
for nombre in ficheros:
    print('Nombre: %-25s %s' % (nombre, fnmatch.fnmatch(nombre,patron)))