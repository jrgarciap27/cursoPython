import datetime

class FestivalMuscial:
    def __init__(self, nombre, pais, estilo_musical):
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical

    def festival_metodo(self):
        print('El mejor festival es. ')

    @classmethod
    def valor_ticket(cls, valor):
        cls.valor_ticket = valor

    @staticmethod
    def dia_evento(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return print ('Es un final de seamana')
        return print('Es un día normal')

#se crea el objeto
festival1 = FestivalMuscial('Creamfields','UK','Dance')

FestivalMuscial.valor_ticket(100)

print(festival1.nombre)
print(festival1.pais)
print(festival1.festival_metodo())

print(festival1.nombre.upper())

festival1.nombre = ('Primavera Sound')
print(festival1.nombre)

#del festival1

print(festival1.valor_ticket)

print(FestivalMuscial.valor_ticket)

dia1 = datetime.date(2021, 11, 30)



FestivalMuscial.dia_evento(dia1);

#print(festival1.dia_evento(dia1));

