import enum


class turno(enum.Enum):
    Matutino = 1
    Vespertino = 2
    Noturno = 3


class turma():
    def __init__(self) :
        self.curso = 'Infoweb'
        self.turno = turno.Vespertino

x = turma.turno
print(x)
