class Pessoa(object):
    def __init__(self, nome):
        self.__nome = nome

a = Pessoa("Nome1")

print(a._Pessoa__nome)

a._Pessoa__nome = "Nome2"

print(a._Pessoa__nome)



print('Um avião \'barato\' e moderno')
print("Um avião \"barato\" e moderno")
print("Um avião 'barato' e moderno")
print('Um avião "barato" e moderno')