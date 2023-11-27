"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que
podem ter seus próprios atributos e métodos.
Os objetos gerados pela classe podem usar seus dados
internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de
classes.
"""

# string = 'Luiz' # str

# print(string.upper())
# print(isinstance(string, str))


class Pessoa:
    ...


p1 = Pessoa()
print(p1)

p1.nome = 'Luiz'
p1.sobrenome = 'Otávio'
print(p1.nome)
print(p1.sobrenome)

p2 = Pessoa()
print(p2)

p2.nome = 'Maria'
p2.sobrenome = 'Joana'
print(p2.nome)
print(p2.sobrenome)