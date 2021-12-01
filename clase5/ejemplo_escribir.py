with open("quijote-ext01.txt", 'r') as file:
    file.seek(18)
    contenido = file.read(42)
    print(contenido)
