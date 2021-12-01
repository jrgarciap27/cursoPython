import io
#fichero = open("quijote_pg2000.txt", 'r')
#for linea in fichero:
#    print(linea)
#fichero.close()

#with open("quijote_pg2000.txt", 'r') as file:
#    contenido = file.read(200)
#    print(contenido)
#    file.close


#with open("quijote_pg2000.txt", 'r') as file:
#    contenido = file.readline()
#    print(contenido)
    #file.close

with open("quijote_pg2000.txt", 'r') as file:
    contenidos = file.readlines(2000)
    for c in contenidos:
        print(c.strip())
