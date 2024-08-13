import enum


class dia(enum.IntFlag):
    segunda = 1 #0000.0001
    terca = 2   #0000.0010
    quarta = 4  #0000.0100
    quinta = 8  #0000.1000
    sexta = 16  #0001.0000
    sabado = 32 #0010.0000
    domingo = 64 #0100.000

hoje = dia.terca
peoo = dia.terca | dia.sexta #União usando o |
fds = dia.sabado | dia.domingo

print(hoje)